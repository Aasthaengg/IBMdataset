n=int(input())
s=input()
a=0
for i in range(n-2):
    if s[i]+s[i+1]+s[i+2]=='ABC':
        a+=1
print(a)