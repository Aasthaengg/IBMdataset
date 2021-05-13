N = int(input())
S = [input() for _ in range(N)]
res = 0
a = 0
b = 0
ba = 0
for s in S:
    if s[0] == "B" and s[-1] == "A":
        ba += 1
    elif s[0] == "B":
        b += 1
    elif s[-1] == "A":
        a += 1
    for i in range(len(s)-1):
        if s[i] == "A" and s[i+1] == "B":
            res += 1
if a == 0 and b == 0:
    res += max(ba - 1, 0)
elif a == N and b == N:
    res += N-1 + ba
else:
    res += min(a, b) + ba
print(res)
