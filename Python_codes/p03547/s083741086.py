x,y = input().split()
d = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
if x==y:
    print("=")
elif d[x]<d[y]:
    print("<")
else:
    print(">")