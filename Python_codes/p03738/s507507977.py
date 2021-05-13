s=[input() for _ in range(2)]
a_len=len(s[0])
b_len=len(s[1])
if s[0]==s[1]:
    print("EQUAL")
elif a_len>b_len:
    print("GREATER")
elif a_len<b_len:
    print("LESS")
else:
    t=sorted(s)
    if s[0]==t[0]:
        print("LESS")
    else:
        print("GREATER")