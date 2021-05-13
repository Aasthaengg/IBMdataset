S = input()
ACGT = ['A', 'C', 'G', 'T']
ans = [0] * len(S)

for i in range(len(S)):
    if S[i] in ACGT:
        cnt = 1
        for j in range(len(S) - i - 1):
            if S[i+j+1] in ACGT:
                cnt += 1
            else:
                ans[i] = cnt
                break
        ans[i] = cnt

print(max(ans))