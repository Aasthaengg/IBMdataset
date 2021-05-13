a = []
while True:
    n = input()
    if n == "0":
        break
    a.append(n)


for i in range(len(a)):
	print("Case ",i+1,": ",a[i],sep="")