s=input()
a=[["","A"],["","A"],["","A"],["","A"]]
for i in range(16):
    num=[]
    for j in range(4):
        num.append(i%2)
        i=i//2
    x=a[0][num[0]]+"KIH"+a[1][num[1]]+"B"+a[2][num[2]]+"R"+a[3][num[3]]
    if s==x:
        print("YES")
        exit()
print("NO")
