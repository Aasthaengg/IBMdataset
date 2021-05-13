s=int(input())
sl=list(str(s))
n=len(sl)
temp=0
for i in range(n):
    for j in range(n-i):
        temp+=(int(sl[i])*(10**j))*(2**(i+max(0,(n-i-j-2))))
print(temp)