S = input()
tmp = ""
cha = ""
lst = []
for i in range(len(S)):
    cha += S[i]
    if(cha != tmp):
        lst.append(cha)
        tmp = cha
        cha = ""
print(len(lst))