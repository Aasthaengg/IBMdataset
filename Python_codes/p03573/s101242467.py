n=list(map(int, input().split()))
a=[]
b=[]
for case in n:
    if len(a)==0:
        a.append(case)
    elif case==a[0]:
        a.append(case)
    else:
        b.append(case)
if len(a)<len(b):
    print(a[0])
else:
    print(b[0])