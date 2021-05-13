s=str(input())
ac=s.count("a")
bc=s.count("b")
cc=s.count("c")

if len(s)==1:
    print("YES")
    exit()

if len(s)==2:
    if max(ac,bc,cc)==2:
        print("NO")
    else:
        print("YES")
    exit()

if (len(s)+2)//3<max(ac,bc,cc):
    print("NO")
else:
    print("YES")