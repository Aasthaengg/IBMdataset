n = int(input())
lh = [int(w) for w in input().split()]

cond = True
nh = lh[0]-1
for i in range(1, n):
    if lh[i] == nh:
        continue
    elif lh[i] > nh:
        nh = lh[i]-1
        continue
    else:
        cond = False
        break

print("Yes" if cond else "No")
