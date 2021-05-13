n = int(input())
b = list(map(int, input().split()))
ans = []

for i in range(n):
    for j in range(n-1-i, -1, -1):
        if b[j] == j+1:
            # print(J+1)
            tmp = b.pop(j)
            ans.append(tmp)
            break
    else:
        print(-1)
        exit()

for a in ans[::-1]:
    print(a)
