S = list(input())
a = len(S)
p = 0
for i in range(a):
    if S[i] != S[a-1-i]:
        p += 1
print(p//2)
