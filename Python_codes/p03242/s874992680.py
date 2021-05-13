s=list(input())
a=[]
for i in s:
    if i=="1":
        a.append("9")
    elif i=="9":
        a.append("1")
    else:
        a.append(i)
print("".join(a))