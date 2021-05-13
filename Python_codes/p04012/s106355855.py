w = list(input())

keys = list(set(w))
cnt = 0
for k in keys:
    kl = len([x for x in w if x == k])
    if kl % 2 != 0:
        cnt += 1

print("Yes" if cnt == 0 else "No")