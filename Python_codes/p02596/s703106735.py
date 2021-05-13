# coding: utf-8
# Your code here!
K=int(input())

mods=[0]*10**6

temp=7
ans=0
while mods[temp%K]==0 and mods[0]==0:
    mods[temp%K]=1
    ans+=1
    temp*=10
    temp+=7
    temp%=K

print(ans if mods[0]==1 else -1)