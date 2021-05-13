n = int(input())
p = list(map(int,input().split()))
q = list(range(1,n+1))
z = 0

for i in range(n-1):
    if p[i] == q[i]:
        p[i+1] = p[i]
        z += 1

if p[-1] == q[-1]:
    print(z + 1)
else:
    print(z)