n = int(input())
for i in [str(i)*3 for i in range(10)]:
    if int(i) >= n:
        print(int(i))
        break
