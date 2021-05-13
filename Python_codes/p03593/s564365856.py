H,W = map(int,input().split())

A = [list(input()) for _ in range(H)]

memo = {}
for a in A:
    for ai in a:
        if ai in memo:
            memo[ai] += 1
        else:
            memo[ai] = 1
            
mod0 = []
mod1_3 = []
mod2 = []
for key, value in memo.items():
    if value % 4 == 0:
        mod0.append(key)
    elif value % 4 == 2:
        mod2.append(key)
    else:
        mod1_3.append(key)

if W % 2 == 0 and H % 2 == 0:
    if len(mod1_3) > 0 or len(mod2) > 0:
        print("No")
    else:
        print("Yes")

elif W % 2 == 0 or H % 2 == 0:
    if H % 2 == 0:
        W, H = H, W
 
    if W // 2 < len(mod2):
        print("No")
    elif len(mod1_3) > 0:
        print("No")
    else:
        print("Yes")

else:
    if len(mod1_3) == 1 and len(mod2) <= H // 2 + W // 2:
        print("Yes")
    else:
        print("No")