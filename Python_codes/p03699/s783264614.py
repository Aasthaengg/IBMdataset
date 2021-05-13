n = int(input())
num_li = []
for i in range(n):
    num_li.append(int(input()))
num_sum = sum(num_li)
if num_sum%10 != 0:
    print(num_sum)
else:
    num_li.sort()
    for i in num_li:
        if i%10 != 0:
            print(num_sum-i)
            exit()
    print(0)
