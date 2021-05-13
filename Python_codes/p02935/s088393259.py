input()
l=sorted(map(int,input().split()))
v=l[0]
for i in l: v=(v+i)/2
print(v)