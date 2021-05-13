n,m = map(int, input().split())
sc = [list(map(int, input().split())) for _ in range(m)]

ans = ["0"] * n
if n>=2: ans[0] = "1"

ok = True
for s,c in sc:
    if s-1==0 and n>=2:
        if ans[s-1] == "1" or ans[s-1] == str(c): ans[s-1] = str(c)
        else: ok = False
    else:
        if ans[s-1] == "0" or ans[s-1] == str(c): ans[s-1] = str(c)
        else: ok = False

if n>=2:
    if ans[0] == "0": ok = False
print(-1 if not ok else "".join(ans))