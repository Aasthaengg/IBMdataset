a1,b1=input().split()
a2,b2=input().split()
a3,b3=input().split()
t=a1+b1+a2+b2+a3+b3
if t.count("1")*t.count("2")*t.count("3")*t.count("4")==0 or max(t.count("1"),t.count("2"),t.count("3"),t.count("4"))==3:
    print("NO")
else:
    print("YES")
