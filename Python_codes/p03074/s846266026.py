n, k = map(int, input().split())
a = input()

one = 0
zero = 0
z = 0
flg = False
num_list = []

if a[0] == '0':
    flg = True
for i in a:
    if one >= 0 and zero == 0 and i == '1':
        one += 1
    elif one == 0 and zero >= 0 and i == '0':
        zero += 1
        z += 1
    elif zero > 0 and i == '1':
        num_list.append(zero)
        one += 1
        zero = 0
    elif one > 0 and i == '0':
        num_list.append(one)
        zero += 1
        one = 0
        z += 1
num_list.append(max(one, zero))

if a[0] == '0':
    num_list.insert(0,0)
num_list.insert(0,0)
num_list.append(0)

if z <= k:
    print(n)
    exit()

n_list = []

sum = 0
for i in range(len(num_list)):
    sum += num_list[i]
    n_list.append(sum)

width = 2*k
if width >= len(num_list):
    print(n)
    exit()

max_num = 0

for i in range(1, len(n_list)-width, 2):
    num = n_list[i+width] - n_list[i-1]
    if num > max_num:
        max_num = num

print(max_num)
