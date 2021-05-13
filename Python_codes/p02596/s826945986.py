k = int(input())

flag = 0
temp = 7
for i in range(k):
    if(temp % k == 0):
        flag = 1
        break
    else:
        temp = temp % k
        temp = temp * 10 % k
        temp = temp + 7

if (flag == 0):
    print("-1")
else:
    print(i+1)