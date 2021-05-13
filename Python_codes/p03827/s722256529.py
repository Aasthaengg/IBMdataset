N = int(input())
S = input().strip()
r = 0
tmp = 0
for s in S:
    if s == "I":
        tmp += 1
        r = max(r, tmp)
    else:
        tmp -= 1
print(r)
