n=input()
if len(n)==1:
    print(int(n))
elif all(i=="9" for i in n[1:]):
    print((len(n) - 1) * 9 + int(n[0]))
elif n[0]!="1" and n[0]!="9" or n[1]=="0":
    print((len(n)-1)*9+int(n[0])-1)
elif n[0]=="1":
    print((len(n)-1)*9)
elif n[0]=="9":
    print((len(n)-1)*9+int(n[1])-1)