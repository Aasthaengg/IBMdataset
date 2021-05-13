DATA=input()
DATA=DATA.split(" ")
A=int(DATA[0])
B=int(DATA[1])

if B%A==0:
    print(A+B)
else:
    print(B-A)
