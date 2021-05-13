a,b,c,d=map(int,input())
if a+b+c+d==7:
    print(str(a)+"+"+str(b)+"+"+str(c)+"+"+str(d)+"="+"7")
elif a+b+c-d==7:
    print(str(a)+"+"+str(b)+"+"+str(c)+"-"+str(d)+"="+"7")
elif a+b-c+d==7:
    print(str(a)+"+"+str(b)+"-"+str(c)+"+"+str(d)+"="+"7")
elif a-b+c+d==7:
    print(str(a)+"-"+str(b)+"+"+str(c)+"+"+str(d)+"="+"7")
elif a-b-c+d==7:
    print(str(a)+"-"+str(b)+"-"+str(c)+"+"+str(d)+"="+"7")
elif a+b-c-d==7:
    print(str(a)+"+"+str(b)+"-"+str(c)+"-"+str(d)+"="+"7")
elif a-b+c-d==7:
    print(str(a)+"-"+str(b)+"+"+str(c)+"-"+str(d)+"="+"7")
elif a-b-c-d==7:
    print(str(a)+"-"+str(b)+"-"+str(c)+"-"+str(d)+"="+"7")