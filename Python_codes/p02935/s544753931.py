n=int(input());a=sorted(map(int,input().split()))
result=(a[0]+a[1])/2
for i in range(2,n): result=(result+a[i])/2
print(result)