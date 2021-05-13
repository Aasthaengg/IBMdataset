import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

N,H = MI()
X = []
for i in range(N):
    a,b = MI()
    X.append((a,0))
    X.append((b,1))

X.sort(reverse=True)

i = 0
ans = 0
while H > 0:
    x,y = X[i]
    if y == 1:
        H -= x
        i += 1
        ans += 1
    else:
        ans += (H+x-1)//x
        break

print(ans)
