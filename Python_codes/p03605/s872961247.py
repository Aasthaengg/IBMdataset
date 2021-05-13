n = str(input())
cnt = 0
for i in n:
    if i == "9":
       cnt += 1
if cnt >= 1:
    print("Yes")
else:
    print("No")