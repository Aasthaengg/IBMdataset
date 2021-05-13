S = input()
X,Y = S[0],S[2]
L = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5}
if L[X]<L[Y]:
    print("<")
elif L[X]>L[Y]:
    print(">")
elif L[X]==L[Y]:
    print("=")
