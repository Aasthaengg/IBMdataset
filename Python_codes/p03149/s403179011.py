ans=[1,4,7,9]
a,b,c,d=map(int,input().split())
list=sorted([a,b,c,d])
if ans==list:
    print("YES")
else:print("NO")