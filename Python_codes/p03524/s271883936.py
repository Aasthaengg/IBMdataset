s=input()

s_a=s.count("a")
s_b=s.count("b")
s_c=s.count("c")

if s_a==0 or s_b==0 or s_c==0:
    if max(s_a, s_b, s_c)>=2:
        print("NO")
    else:
        print("YES")
else:
    if max(s_a, s_b, s_c)-min(s_a, s_b, s_c)>=2:
        print("NO")
    else:
        print("YES")
