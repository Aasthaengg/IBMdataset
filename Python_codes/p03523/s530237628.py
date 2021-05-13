S = list(input())

AK = list('AKIHABARA')

if S == AK:
    ans = 'YES'
elif len(S) >= len(AK):
    ans = 'NO'
else:
    for i in range(len(S)):
        if S[i] != AK[i]:
            S.insert(i, AK[i])
    if len(S) > len(AK):
        ans = 'NO'
    else:
        for i in range(len(S)):
            if S[i] != AK[i]:
                S.insert(i, AK[i])

        if len(S) > len(AK):
            ans = 'NO'
        else:
            if len(S) != len(AK):
                S.append('A')

            if S == AK:
                ans = 'YES'
            else:
                ans = 'NO'

print(ans)
