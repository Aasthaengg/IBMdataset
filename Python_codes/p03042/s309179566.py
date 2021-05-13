S = input()
ans='None'
if 1<=int(S[:2]) <=12 and 1<=int(S[2:])<=12:
    ans='AMBIGUOUS'
elif 1<=int(S[:2])<=12:
    ans='MMYY'
elif 1<=int(S[2:])<=12:
    ans='YYMM'
else:
    ans='NA'
print(ans)