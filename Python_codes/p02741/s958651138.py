retu = "1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51"

retu = retu.split(",")
retuint=[]
for i in retu :
	retuint.append(int(i))

index=input()

print(retuint[int(index)-1])