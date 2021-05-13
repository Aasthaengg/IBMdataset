s = input()
i = 0
p = []
tmp =[]
n = len(s)
while i<n-1:
    if(s[i]=="A" or s[i:i+2]=="BC"):
        if s[i]=="A":
            
            tmp.append(1)
            i+=1
        else:
            tmp.append(0)
            i+=2

    else:
        p.append(tmp)
        tmp = []
        i+=1
p.append(tmp)
res = 0
for i in range(len(p)):
    anum = 0
    bcnum = 0
    for j in range(len(p[i])):
        if p[i][j]:anum+=1
        else:
            res += (anum)
print(res)
