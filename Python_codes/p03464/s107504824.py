K = int(input())
A = list(map(int, input().split()))
mi = 2
ma = 2
for i in range(K-1, -1, -1):
    a = A[i]
    if ma < a:
        print(-1)
        exit()
    mi = ((mi-1)//a+1)*a
    ma = ma//a*a+a-1
    if mi > ma:
        print(-1)
        exit()
print(mi, ma)
