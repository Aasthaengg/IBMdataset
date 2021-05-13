x = {}
for i in range(4):
    for j in range(3):
        for k in range(10):
            i,j,k = str(i), str(j), str(k)
            x[i+j+k] = 0

n = int(input())
for i in range(n):
    i,j,k,l = map(int, input().split())
    key = str(i-1)+str(j-1)+str(k-1)
    x[key] = x[key] + int(l)

for i in range(4):
    for j in range(3):
        for k in range(10):
            i,j,k = str(i), str(j), str(k)
            if k != "9":
                print(" " + str(x[i+j+k]), end='')
            else:
                print(" "+ str(x[i+j+k]))
    if int(i) + 1 < 4:
        print("#"*20)