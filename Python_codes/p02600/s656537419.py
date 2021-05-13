a = 400
b = 199
L1= []
L2 = []
for i in range(8):
    L1.append(a+200*(i))
    L2.append(a+200*(i)+b)


n = int(input())
for i in range(8):
    if L1[i] <= n <= L2[i]:
        print(8-i)