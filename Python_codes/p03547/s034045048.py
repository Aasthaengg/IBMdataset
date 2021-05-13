X,Y=input().split()
number={"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
if number[X]==number[Y]:
    print("=")
elif number[X]<number[Y]:
    print("<")
else:
    print(">")