x = input("")
for i in range(3):
    alist = list(map(int,x))
    result = sum(alist)
    x = str(result)
if result % 9 == 0 :
    print("Yes")
else:
    print("No")