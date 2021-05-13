S = input()
ANS = {0:'NA', 1:'YYMM', 2:'MMYY', 3:'AMBIGUOUS'}
ans = 0
if '00' <= S[:2] <= '99' and '01' <= S[2:] <= '12':
    ans += 1
if '00' <= S[2:] <= '99' and '01' <= S[:2] <= '12':
    ans += 2
print(ANS[ans])
