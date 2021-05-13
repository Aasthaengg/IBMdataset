n=int(input())
s,t=input().split()
a=[]
for i in range(n):
    a+=[s[i]+t[i]]
print("".join(a))