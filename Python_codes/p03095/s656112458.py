_=input()
s=input()
ans=1
for i in set(s):
    ans*=s.count(i)+1
    ans%=10**9+7
print(ans-1)