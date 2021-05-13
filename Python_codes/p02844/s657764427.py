N = int(input())
S = input()
ans = 0
for i in range(10):
    for j in range(10):
        ii = S.find(str(i))
        if ii == -1:
            break
        for k in range(10):
            jj = S[ii+1::].find(str(j))
            if jj == -1:
                break
            jj += ii+1
            kk = S[jj+1::].find(str(k))
            if kk != -1:
                ans += 1
print(ans)