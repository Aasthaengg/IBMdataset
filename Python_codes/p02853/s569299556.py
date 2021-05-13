a,b=map(int,input().split())
n=max(0,4-a)*10**5+max(0,4-b)*10**5
print(n+4*10**5 if a==b and a==1 else n)