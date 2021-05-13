S = input()

ans = 'NA'
L = int(S[ : 2])
R = int(S[2 :])

if 13 > L > 0 and 13 > R > 0:
    ans = 'AMBIGUOUS'
elif 13 > R > 0:
    ans = 'YYMM'
elif  13 > L > 0:
    ans = 'MMYY'

print(ans)