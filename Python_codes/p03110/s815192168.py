ans=0
for i in range(int(input())):
    x,u=input().split()
    if u=='BTC':
        ans+=float(x)*380000
    else:
        ans+=int(x)
print(ans)