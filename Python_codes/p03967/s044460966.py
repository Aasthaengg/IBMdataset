s = input()
n = len(s)
go = 0
pa = 0
score = 0
for i in range(n):
    if s[i] == "g":
        go += 1
    else:
        if go > pa:
            pa +=1
        else:
            go += 1
            score -=1
print(score+(go-pa)//2)