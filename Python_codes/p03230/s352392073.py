import math
n = int(input())
if n == 1:
    print("Yes")
    print(2)
    print("1 1")
    print("1 1")
    exit()

ok = False
for i in range(2, int(math.sqrt(n*2)+1)):
    if n*2 % i == 0 and n*2 // i == i+1:
        ok = True
        size = i
        break
if ok:
    ans = [[0] * size for _ in range(size+1)]
    val = 1
    for i in range(0, size+1):
        for j in range(i, size):
            ans[i][j] = val
            val += 1
    val = 1
    for i in range(0, size):
        for j in range(i, size):
            ans[1+j][i] = val
            val += 1
    print("Yes")
    print(size+1)
    for line in ans:
        print(str(size) + " " + " ".join([str(item) for item in line]))

else:
    print("No")