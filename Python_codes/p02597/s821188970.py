N = int(input())
C = input()
rcount = len([1 for c in C if c == "R"])

count = 0
r = 0
w = 0
for i in range(rcount):
    c = C[i]
    if c == "W":
        if r > 0:
            r -= 1
            count += 1
        else:
            w += 1
    c = C[N-i-1]
    if c == "R":
        if w > 0:
            w -= 1
            count += 1
        else:
            r += 1
ans = count + w
print(ans)