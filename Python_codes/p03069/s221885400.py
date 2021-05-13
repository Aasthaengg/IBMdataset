n=int(input())
s=input()
a=[0]
for i in s:
    if i==".":a+=[a[-1]+1]
    else:a+=[a[-1]]
w=s.count(".")
print(min(i-a[i]*2+w for i in range(n+1)))