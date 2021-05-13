s=list(input())
S=[]
for i in range(len(s)):
    S.append(int(s[i]))
if 1<=S[2]*10+S[3] and S[2]*10+S[3]<=12:
    if 1<=S[0]*10+S[1] and S[0]*10+S[1]<=12:
        print('AMBIGUOUS')
    else:
        print('YYMM')
else:
    if 1<=S[0]*10+S[1] and S[0]*10+S[1]<=12:
        print('MMYY')
    else:
        print('NA')