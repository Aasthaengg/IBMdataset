b = []
count = []
while True:
    inp = input()
    a = inp.split()
    a[0] = int(a[0])
    a[1] = int(a[1])
    if a[0] == 0 and a[1] == 0:
        break
    else:
        b.append(a)
        count.append(0)
for i in range(len(b)):
    for j in range(1,b[i][0]):
        for k in range(j+1,b[i][0]):
               for l in range(k+1,b[i][0]+1):
                    if b[i][1]-j-k-l == 0:
                        count[i] += 1
for i in range(len(count)):
    print(count[i])
