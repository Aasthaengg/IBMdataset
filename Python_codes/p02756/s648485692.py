from collections import deque
s = input()
q = int(input())
Q = [list(input().split()) for _ in range(q)]

ans = deque(s)
ok = True
for v in Q:
    if v[0] == "1":
        if ok: ok = False
        else: ok = True
    else:
        if v[1] == "1":
            if ok: ans.appendleft(v[2])
            else: ans.append(v[2])
        else:
            if ok: ans.append(v[2])
            else: ans.appendleft(v[2])
ans = list(ans)
if not ok: ans = ans[::-1]
print("".join(ans))