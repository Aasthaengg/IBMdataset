n=int(input());a=list(map(int,input().split()));count=0
for i in range(n-2): count+=a[i:i+3][1]==sorted(a[i:i+3])[1]
print(count)