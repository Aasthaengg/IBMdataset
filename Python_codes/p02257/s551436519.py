def check_prime(num):
    if num == 2:
        return True

    if num < 2 or num % 2 == 0:
        return False

    return pow(2,num-1,num) == 1

cnt_num = int(input())
dataset = [int(input()) for i in range(cnt_num)]

count = 0
for i in dataset:
    if check_prime(i):
        count += 1

print(count)