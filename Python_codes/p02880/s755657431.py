n = int(input())
flag = 0

for i in range(1,10):
    if n%i == 0 and n//i<10:
        print('Yes')
        flag = 1
        break

if flag == 0:
    print('No')
