ca = ord('a')
A = [ord(c) - ca for c in input()]

cnts = [0]*26
ans = 1
for i, a in enumerate(A):
    ans += i - cnts[a]
    cnts[a] += 1
print(ans)