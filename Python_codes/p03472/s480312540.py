N,H = map(int,input().split())
B = []
max_attack = 0
for i in range(N):
    a,b = map(int,input().split())
    max_attack = max(a,max_attack)
    B.append(b)

B.sort(reverse=True)
ans = 0

for b in B:
    if max_attack <= b:
        H -= b
        ans += 1
        if H <= 0:
            break
    else:
        break

if 0 < H:
    if H%max_attack == 0:
        ans += H//max_attack
    else:
        ans += 1+H//max_attack
print(ans)
