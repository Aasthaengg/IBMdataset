N = int(input())

i = 1
num = 0
while True:
    num += i
    if num >= N:
        break
    i += 1

del_num = num - N
min_num = i
for i in range(1, min_num+1):
    if i != del_num:
        print(i)