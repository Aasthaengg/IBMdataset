N = int(input())
d = list(map(int, input().split()))
# l = []
total = 0
for i,iv in enumerate(d):
    for j,jv in enumerate(d):
        if i < j:
            # l.append([iv,jv])
            total += iv * jv
# print(l)
print(total)