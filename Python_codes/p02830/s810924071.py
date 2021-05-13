n=int(input())
s,t=map(str,input().split())
result=''
for i in range(0,n):
    result+=s[i]
    result+=t[i]
print(result)
