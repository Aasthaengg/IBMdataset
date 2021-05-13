N = int(input())
S = "A" + input()
r, g, b = 0, 0, 0

for s in S[1:]:
    if s == "R":
        r += 1
    elif s == "G":
        g += 1
    else:
        b += 1

pat = r*g*b

for i in range(1, N-1):
    for j in range(i+1, N):
        k = 2*j - i
        if (j+1 <= k <= N) and S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
            pat -= 1

print(pat)

