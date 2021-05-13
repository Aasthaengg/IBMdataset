S=input()
mmyy=1<=int(S[:2])<=12
yymm=1<=int(S[2:])<=12
l=[['AMBIGUOUS','MMYY'],['YYMM','NA']]
print(l[not mmyy][not yymm])