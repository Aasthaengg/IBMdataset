n,k = map(int,input().split())

max_num = 0
num = n / k
if n % k != 0:
    max_num = num + 1
else:
    max_num = num

print(int(max_num - num))