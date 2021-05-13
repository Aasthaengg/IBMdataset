input()
s = list(map(int,input().split()))
t = sorted(s)
if s==t:
    print('YES')
else:
    ans = sum(1 for i,j in zip(s,t) if i!=j)
    print('NO' if ans>2 else 'YES')