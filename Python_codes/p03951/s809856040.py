N = int(input())
s = input().strip()
t = input().strip()
lmin = 2*N
for i in range(1,N+1):
    if s[-i:]==t[:i]:
        lmin = min(lmin,2*N-i)
print(lmin)