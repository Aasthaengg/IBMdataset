S = input()
S = sorted(S)
alpha = [chr(i)for i in range(97,97+26)]
ans = "None"
for W in alpha:
    if not(W in S):
        ans = W
        break
print(ans)
