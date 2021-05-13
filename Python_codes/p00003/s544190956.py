num=int(input())
for i in range(num):
    list=[int(i) for i in input().split()]
    list.sort();
    if pow(list[0],2) + pow(list[1],2) == pow(list[2],2):
        print('YES')
    else:
        print('NO')