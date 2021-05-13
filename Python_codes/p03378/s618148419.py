s = input().split()
n = int(s[0])
m = int(s[1])
x = int(s[2])

masu = []
for i in range(n + 1):
    masu.append(False)

v = input().split()
for i in range(m):
    z = int(v[i])
    masu[z] = True

left = 0
right = 0

for i in range(x):
    if masu[i]:
        left += 1

for i in range(x, len(masu)):
    if masu[i]:
        right += 1



answer = min(left, right)
print(answer)