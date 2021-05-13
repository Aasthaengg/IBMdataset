S = input()
ans = 0
for i in range(1, len(S)//2):
    if S[:i] == S[i:i+i]:
        ans = 2*i
print(ans)
