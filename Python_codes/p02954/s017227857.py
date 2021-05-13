S = str(input())
n = int(len(S))
ans = [str(0) for i in range(n)]
cntLo = 0
cntRo = 0
cntLe = 0
cntRe = 0
for i in range(n-1):
    if S[i] == "R" and S[i+1] == "L":
        j = 1
        k = 1
        while i-j >= 0 and S[i-j] == "R":
            if j % 2 == 0:
                cntRe += 1
            else:
                cntRo += 1
            j += 1
        while i+1+k <= n-1 and S[i+1+k] == "L":
            if k % 2 == 0:
                cntLe += 1
            else:
                cntLo += 1
            k += 1
        ans[i] = str(cntRe + cntLo+1)
        ans[i+1] = str(cntRo + cntLe+1)
        cntLo = 0
        cntRo = 0
        cntLe = 0
        cntRe = 0
print(" ".join(ans))