n,*a=map(int,open(0).read().split())
m=max(a)
b=m//2
o=min(a)
for A in a:
 if abs(A-b)<abs(o-b):o=A
print(m,o)
