import collections 
na=int(input())
n=1
mod = 10**9+7
for i in range(2,na+1):
    n*=i
#print(n)

n_break=[]
i=2
while i<=n:
    if n%i==0:
        n_break.append(i)
        n=n//i
    else:
        i+=1
#print(n_break)
ans=1
count=collections.Counter(n_break)
for v in count.values():
    ans*=(v+1)  #約数の総数

print(ans%mod)
