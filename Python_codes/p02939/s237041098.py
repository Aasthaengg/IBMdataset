S = input()

ans = [""]
j = 0

for i in range(1, len(S) + 1):
    s = S[j:i]
    if s != ans[-1]:
        ans.append(s)
        j = i
    

print(len(ans) - 1)