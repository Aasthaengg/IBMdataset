l=[int(input()) for i in range(6)]
k=l[5]
c=0
for i in range(4):
    for j in range(i+1,5):
        if abs(l[j]-l[i])<=k:
            c+=1
if c==10:
    print("Yay!")
else:
    print(":(")


