S=int(input())
x=S//100
y=S%100
yymm=1<=y<=12
mmyy=1<=x<=12
ans=""
if yymm and mmyy:
    ans="AMBIGUOUS"
elif yymm:
    ans="YYMM"
elif mmyy:
    ans="MMYY"
else:
    ans="NA"
print(ans)