n1, n2, n3 = list(map(int, input().split()))
x = min(n2,n3)
if n2+n3<=10:
    y=0
else:
    y = max(n2+n3-n1,0)
print(x,y)