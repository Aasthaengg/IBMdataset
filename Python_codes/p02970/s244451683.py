n,d=map(int,input().split())
if n%(d*2+1) == 0:print(int(n/(d*2+1)))
else:print(int(n/(d*2+1)) + 1)