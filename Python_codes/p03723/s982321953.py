A,B,C = [int(i) for i in input().split()]

if A%2+B%2+C%2 != 0:
    print(0)
    exit()


p = [set([A,B,C])]
cnt = 1
while True:
    a = B//2+C//2
    b = A//2+C//2
    c = A//2+B//2
    if a%2+b%2+c%2 != 0:
        print(cnt)
        exit()
    if set([a,b,c]) in p:
        print(-1)
        exit()
    else:
        p.append(set([a,b,c]))
        A = a
        B = b
        C = c
        cnt += 1
