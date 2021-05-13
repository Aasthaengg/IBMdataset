n = int(input())

for i in range(1,10):
    if int(n)>int(str(i)*3):
        continue
    print(str(i)*3)
    break