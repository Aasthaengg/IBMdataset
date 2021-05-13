n = int(input())
num = [1,2,4,8,16,32,64,101]
for i in range(7):
    if num[i] <= n < num[i+1]:
        print(num[i])