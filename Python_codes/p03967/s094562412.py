S = input()
g = 0
p = 0

ans = 0

for i, s in enumerate(S):
    if i&1:
        m = "p"
    else:
        m = "g"
    
    if s=="g" and m=="p":
        ans += 1
    elif s=="p" and m=="g":
        ans -= 1

print(ans)