X,Y = map(str,input().split())
dic = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
if dic[X]<dic[Y]:
    print("<")
elif dic[X]>dic[Y]:
    print(">")
elif dic[X] ==dic[Y]:
    print("=")