N = int(input())
s = input().strip()
t = input().strip()
ind = -1
for i in range(N):
    x = s[i:]
    y = t[:N-i]
    if x==y:
        ind = i
        break
if ind>=0:
    print(N+i)
else:
    print(2*N)