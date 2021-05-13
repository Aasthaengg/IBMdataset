n=int(input())
xu=[]
total=0
for i in range(n):
    xu.append([x for x in input().split()])

a=380000.0
for i in range(n):
    if xu[i][1]=="JPY":
        total+=float(xu[i][0])
    else:
        total+=float(xu[i][0])*a
print(total)
