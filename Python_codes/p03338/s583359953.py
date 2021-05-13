N = int(input())
S = input()
ans = 0
for i in range(N-1):
    c = 0
    for j in range(26):
        if chr(j+97) in S[:i+1] and chr(j+97) in S[i+1:]:
            c += 1
    if c > ans:
        ans = c
print(ans)
