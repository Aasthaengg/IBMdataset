K = int(input())

lis = [49] * 50

dif = K // 50
amari = K % 50

for i in range(50):

    lis[i] += dif

    if i < amari:
        lis[i] += 50 - amari + 1
    else:
        lis[i] -= amari

print (50)

print (" ".join(map(str,lis)))
