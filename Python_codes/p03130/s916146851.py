 #B-Path
a1,b1=map(int,input().split( ))
a2,b2=map(int,input().split( ))
a3,b3=map(int,input().split( ))
x=[a1,b1,a2,b2,a3,b3]
y=[x.count(i) for i in range(1,5)]
if max(y)==3 or min(y)==0:
    print("NO")

else:
    print("YES")