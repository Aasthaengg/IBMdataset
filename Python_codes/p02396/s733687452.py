num = []
while True:
    n = int(input())
    if n != 0:
        num.append(n)
    else:
        break
for i in range(len(num)):
    print("Case " + str(i + 1) + ": " + str(num[i]))