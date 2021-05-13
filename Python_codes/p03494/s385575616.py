n = input().split()
a = list(map(int, input().split() ))
count = 0

while(True):
    T = False
    for i in range(len(a)):
        if a[i]%2 != 0:
            T=True
        else:
            a[i] = a[i] / 2

    if T:
        break

    count+=1

print(count)
