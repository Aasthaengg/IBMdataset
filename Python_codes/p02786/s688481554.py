H = int(input())
num = {}
lis = [H]

h = H
while h > 1:
    h //= 2
    num[h] = 0
    lis = [h] + lis

num[1] = 1

for n in lis[1:]:
    num[n] = 2*num[n//2] + 1

print(num[H])
