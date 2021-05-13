x=int(input())
lst=[1]
for i in range(2,32):
    for j in range(2,10):
        if i**j<=1000:
            lst.append(i**j)

for i in range(1000):
    a=x-i
    if a in lst:
        print(a)
        exit()