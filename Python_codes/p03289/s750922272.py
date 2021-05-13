S = input()
if S[0]=="A" and S[2:-1].count("C")==1:
    b = 0
    for s in S:
        if not 97<=ord(s)<=122:
            b += 1
    if b==2:
        print("AC")
    else:
        print("WA")
else:
    print("WA")