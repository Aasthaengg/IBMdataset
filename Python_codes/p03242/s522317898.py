n = input()



if n[0] == "1":
    a = 9
elif n[0] == "9":
    a = 1

if n[1] == "1":
    b = 9
elif n[1] == "9":
    b = 1

if n[2] == "1":
    c = 9
elif n[2] == "9":
    c = 1

d = a*100 + b*10 + c


print(d)