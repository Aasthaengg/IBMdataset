s=list(input())
a=s.count("a")
b=s.count("b")
c=s.count("c")
l1=[a,b,c]
l1.sort()
if l1[0]==0 and l1[1]==1 and l1[2]==1:
    print("YES")
elif min(a,b,c)!=0 and max(a,b,c)-min(a,b,c)<=1:
    print("YES")
elif a+b+c==max(a,b,c) and max(a,b,c)==1:
    print("YES")
else:
    print("NO")
