S = input()
n = len(S)
prev = '-1'
ans = 0
obj = S[0]
for i in range(n):
    # print(prev, obj)
    if prev != obj:
        prev = obj
        ans += 1
        if i+1 < n:
            obj = S[i+1]
    else:
        if i+1 < n:
            obj += S[i+1]
    # if prev != S[i]:
    #     ans += 1
    #     prev = S[i]
    # else:
    #     prev += S[i]
    # print(prev)

print(ans)