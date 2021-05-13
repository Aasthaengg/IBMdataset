a = input()
b = input()
c = input()
Sa,Sb,Sc = [],[],[]
for x in a:
    Sa.append(x)
for x in b:
    Sb.append(x)
for x in c:
    Sc.append(x)

x = Sa.pop(0)
while True:
    
    if x == "a":
        if Sa == []:
            print("A")
            break
        else:
            x = Sa.pop(0)
    elif x == "b":
        if Sb == []:
            print("B")
            break
        else:
            x = Sb.pop(0)
    else :
        if Sc == []:
            print("C")
            break
        else:
            x = Sc.pop(0)
