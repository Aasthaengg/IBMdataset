n=int(input())
c=0
for i in range(n):
    a,b=map(str,input().split())
    if b=="BTC":
        c+=float(a)*380000
    else:
        c+=float(a)
print(c)