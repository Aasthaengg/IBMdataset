O = input()
E = input()
psw = ""
for i in range(len(E)):
    psw = psw + O[i] + E[i]
if len(O) == len(E):
    print(psw)
else:
    print(psw+O[-1])