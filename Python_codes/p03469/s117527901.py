S = str(input())

a = S[:4]
b = S[4:]

if a == "2017":
    a = "2018"
    i = a + b
    print(i)
else:
    print(S)