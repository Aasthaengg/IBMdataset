k = int(input())
a = 7
flag = 0
for i in range(1,k+1):
    if a % k == 0:
        print(i)
        flag = 1
        break
    a = 10*(a%k) + 7
if flag == 0:
    print(-1)
#     print(a)