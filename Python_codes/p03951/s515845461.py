N = int(input())
s = input()
t = input()
if s == t:
    print(N)
    exit(0)
ans = 2*N
for k in range(1,N+1):
    if s[k:] == t[:-k]:
        ans = min(ans,2*N-len(s[k:]))
print(ans)
