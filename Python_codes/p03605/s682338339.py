#abc073
n=input()
flag=False
for c in n:
    if c=="9":
        flag=True
        break
if flag:
 	print("Yes")
else:
 	print("No")
