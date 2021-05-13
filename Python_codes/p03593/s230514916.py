H, W = map(int, input().split())
ctr = [0] * 26
for _ in range(H):
    s = str(input())
    for a in s:
        ctr[ord(a) - 97] += 1

# print(ctr)

def count(ctr):
    odd = 0
    two = 0
    four = 0
    for n in ctr:
        if n == 0: continue
        if n % 2 == 1: odd += 1
        elif n % 4 == 0: four += 1
        elif n % 2 == 0: 
            two += 1
            if n >= 4:
                four += 1
    return odd, two, four  

def f():
    odd, two, four = count(ctr)
    # print(odd, two, four)
    if (H * W) % 2 == 1:
        if odd > 1: return False
        if two > (H - 1) // 2 + (W - 1) // 2: return False
        return True
    if H % 2 == 0 and W % 2 == 0:
        if odd > 0 or two > 0: return False
        return True
    else:
        if odd > 0: return False
        if H % 2 == 1:
            tmp = W
        else:
            tmp = H
        if two > tmp // 2: return False
        return True

if f():
    print("Yes")
else:
    print("No")