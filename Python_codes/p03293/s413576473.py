S = list(input().strip())
T = list(input().strip())
f = False
for _ in range(len(T)+1):
    if S == T:
        f = True
        break
    t = T.pop(0)
    T.append(t)

print("Yes" if f else "No")
