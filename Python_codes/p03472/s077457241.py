N,H = map(int,input().split())
kill = []
throw = []
ans = 0
for i in range(N):
    a,b = map(int,input().split())
    kill.append(a)
    throw.append(b)
throw.sort()
throw.reverse()
const = max(kill)
for j in throw:
    if j <= const:
        break
    else:
        H -= j
        ans += 1
        if H <= 0:
            break
if H > 0:
    time = H//const
    if H % const == 0:
        ans += time
    else:
        ans += time+1
print(ans)