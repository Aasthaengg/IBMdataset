S = input()
K = int(input())

N = len(S)

m= 1
for m in range(1, N):
    if S[m] != S[m-1]:break
    else: m += 1

def calc(s):
    ans = 0
    pre = s[0]
    for ss in s[1:]:
        if ss == pre:
            ans += 1
            pre = '0'
        else: pre = ss
    return ans

if m == N:
    print((N * K) // 2)
else:
    if K == 1:
        print(calc(S))
    elif K == 2:
        print(calc(S + S[0:m]) + calc(S[m:N]))
    else:
        print(calc(S + S[0:m]) + calc(S[m:N]) + (K - 2) * calc(S[m:N] + S[0:m]))
