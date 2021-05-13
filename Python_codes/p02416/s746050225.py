Ans=[]
while True:
    l=list(input())
    if l==["0"]:
        break
    else:
        su=0
        for s in l:
            su+=int(s)
        Ans.append(su)
for a in Ans:
    print(a)

