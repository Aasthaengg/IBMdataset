A,B,C = map(int,input().split())
if A%2 != 0 or B%2 != 0 or C%2 != 0:
    print(0)
    exit()
if A*2 == B+C and B*2 == A+C and C*2 == A+B:
    print(-1)
    exit()
ans = 0
for i in range(10000):
    a = A//2
    b = B//2
    c = C//2
    if A%2 == 0 and B%2 == 0 and C%2 == 0:
        ans += 1
        A = b+c
        B = a+c
        C = a+b
    else:
        print(ans)
        exit()