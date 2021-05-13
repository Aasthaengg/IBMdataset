import collections

def gcd(a,b):
  if b==0:
    return a
  else:
    return gcd(b,a%b)

mod=10**9+7
n=int(input())
dic=collections.defaultdict(int)
cnt=0
for _ in range(n):
  a,b=map(int,input().split())
  if a!=0 and b!=0:
    g=gcd(abs(a),abs(b))
    if a*b>0:
      dic[(abs(a)//g,abs(b)//g)]+=1
    else:
      dic[(-abs(a)//g,abs(b)//g)]+=1
  else:
    if a==0 and b==0:
      cnt+=1
    elif a==0:
      dic[(0,1)]+=1
    elif b==0:
      dic[(1,0)]+=1
ans=1
s=set()
for a,b in dic.keys():
  if (a,b) in s:
    continue
  s.add((a,b))
  if a!=0 and b!=0:
    if a>0:
      s.add((-b,a))
      cnt1=dic[(a,b)]
      if (-b,a) in dic:
        cnt2=dic[(-b,a)]
      else:
        cnt2=0
      ans*=(pow(2,cnt1,mod)+pow(2,cnt2,mod)-1)%mod
      ans%=mod
    elif a<0:
      s.add((b,-a))
      cnt1=dic[(a,b)]
      if (b,-a) in dic:
        cnt2=dic[(b,-a)]
      else:
        cnt2=0
      ans*=(pow(2,cnt1,mod)+pow(2,cnt2,mod)-1)%mod
      ans%=mod
  else:
    s.add((b,a))
    cnt1=dic[(a,b)]
    if (b,a) in dic:
      cnt2=dic[(b,a)]
    else:
      cnt2=0
    ans*=(pow(2,cnt1,mod)+pow(2,cnt2,mod)-1)%mod
    ans%=mod
print((ans+cnt-1)%mod)