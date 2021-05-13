input()
p,*v=sorted(map(int,input().split()))
for x in v:p=(p+x)/2
print(p)