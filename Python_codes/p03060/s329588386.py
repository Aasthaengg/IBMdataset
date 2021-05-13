n=int(input())
vl=list(map(int,input().split()))
cl=list(map(int,input().split()))
a=0
for v,c in zip(vl,cl):
  if v>c:
    a+=v-c
print(a)