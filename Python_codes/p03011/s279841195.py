p,q,r = map(int,input().split())
s = p + q + r
print(min(s-p,s-q,s-r))
