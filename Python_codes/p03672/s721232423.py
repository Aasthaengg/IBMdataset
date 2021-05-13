S = input()
N = len(S)
ans = 0
for l in range(N//2+1):
    flag = True
    for i in range(l):
        if S[i] != S[i+l]:
            flag = False
            break
    if flag:
        if l*2 < N:
            ans = max(ans, l)
print(ans*2)