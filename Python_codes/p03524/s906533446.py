s=input()
t = set(s)
if len(s) ==1:
    print("YES")
    exit(0)
elif len(s) == 2 and len(t) ==2:
    print("YES")
    exit(0)
if len(t) != 3:
    print("NO")
else:
    a = s.count("a")
    b = s.count("b")
    c = s.count("c")
    M = max(a,b,c)
    m = min(a,b,c)
    if M - m >1 :
        print("NO")
    else:
        print("YES")

