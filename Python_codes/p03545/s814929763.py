s=input()
a,b,c,d=int(s[0]),int(s[1]),int(s[2]),int(s[3])
if a+b+c+d==7:
    print("{}+{}+{}+{}=7".format(a,b,c,d))
elif a+b+c-d==7:
    print("{}+{}+{}-{}=7".format(a,b,c,d))
elif a+b-c+d==7:
    print("{}+{}-{}+{}=7".format(a,b,c,d))
elif a-b+c+d==7:
    print("{}-{}+{}+{}=7".format(a,b,c,d))
elif a+b-c-d==7:
    print("{}+{}-{}-{}=7".format(a,b,c,d))
elif a-b+c-d==7:
    print("{}-{}+{}-{}=7".format(a,b,c,d))
elif a-b-c+d==7:
    print("{}-{}-{}+{}=7".format(a,b,c,d))
else:
    print("{}-{}-{}-{}=7".format(a,b,c,d))