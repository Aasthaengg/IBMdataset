N = int(input())
for i in range(10):
    if int(str(i)*3) < N <= int(str(i+1)*3):
        break
print(str(i+1)*3)
