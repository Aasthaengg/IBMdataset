big = str(input())
num = 0
for x in range(len(big)):
    num += int(big[x])
if num % 9 == 0:
    print("Yes")
else:
    print("No")
