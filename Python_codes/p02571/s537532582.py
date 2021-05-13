S = input()
T = input()
n = len(T)

ans = 10**9
for i in range(n,len(S)+1):
    dummy = S[i-n:i]
    tmp = 0
    for j in range(n):
        if dummy[j] != T[j]:
            tmp +=1

    if ans > tmp:
        ans = tmp
print(ans)