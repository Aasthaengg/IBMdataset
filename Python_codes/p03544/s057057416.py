n = int(input())
l = [0]*87
l[0] = 2
l[1] = 1

for i in range(2,87):
    tmp = l[i-2] + l[i-1]
    l[i] = tmp

print(l[n])