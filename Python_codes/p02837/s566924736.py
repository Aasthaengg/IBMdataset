N = int(input())

A = [[] for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(int(input())):
        A[i].append(list(map(int, input().split())))
#A

X = list(range(1, N+1))

n = N
ans = 0
for bit in range(2**n):
    Pick = []
    for j in range(n):
        mask = 1 << j
        if bit & mask:
            Pick.append(X[j])
#    print()
#    print(Pick)
    flag = True
    for pick in Pick:
        for xy in A[pick]:
            x = xy[0]
            y = xy[1]
            if y == 1 and x in Pick:
                flag *= True
            elif y == 0 and not(x in Pick):
                flag *= True
            else:
                flag *= False
#            print(x, y, flag)
#        print(pick, flag)
    if flag == True:
        ans = max(ans, len(Pick))
print(ans)                    