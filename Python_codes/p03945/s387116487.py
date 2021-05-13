S = input()
N = len(S)

if N==1:
    print(0)
else:
    b = S[0]
    ans = 0
    for i in S[1:]:
        if i!=b:
            ans += 1
            b = i
    print(ans)
