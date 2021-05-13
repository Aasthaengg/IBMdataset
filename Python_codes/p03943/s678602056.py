a,b,c=[int(x) for x in input().split(" ")]
if (a+b)==c or (a+c)==b or (b+c)==a:
    print("Yes")
else:
    print("No")
