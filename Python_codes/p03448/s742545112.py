a_500 = int(input())
b_100 = int(input())
c_50 = int(input())
kadai = int(input())
sum_coin = 0
count = 0
sum_list = []

for n in range(a_500 + 1):
    for m in range(b_100 + 1):
        for l in range(c_50 + 1):
            sum_list.append((500*n) + (100*m) + (50*l))
print(sum_list.count(kadai))