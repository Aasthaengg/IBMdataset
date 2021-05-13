N = int(input())
A = list(map(int, input().split()))

r = [0] * (N//2)
Nn =  N//2
r.extend(A[Nn:])

for i in range(Nn):
    n = Nn - i - 1
    s = 0
    for j in range(N//(n+1)):
        if r[(n+1)*(j+1) -1] == 1:
            s += 1
    s += A[n]
    s %= 2
    r[n] = s

x = ''
y = 0
k = 0
for num, i in enumerate(r):
    if i == 1:
        k = 1
        x += str(num+1) + ' '
        y += 1

print(y)
if k:
    print(x)
