n=int(input())
s=str(input())
a=''
for i in range(len(s)-n-1):
    a+=s[i]+s[i+n+1]
print(a)