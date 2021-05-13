n = int(input())
c = list(input())
r = [0]
w = [0]
for i in range(n):
    if c[i] == "W":
        w.append(w[-1]+1)
    else:
        w.append(w[-1])
    if c[i] == "R":
        r.append(r[-1]+1)
    else:
        r.append(r[-1])

ans = float('inf')
for i in range(n+1):
    r_left = r[i]
    r_right = r[-1] - r[i]
    w_left = w[i]
    w_right = w[-1] - w[i]
    
    ans = min(ans,max(r_right,w_left))

print(ans)