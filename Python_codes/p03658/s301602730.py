data = [int(i) for i in input().split(' ')]
K = data[1]
ls = sorted([int(i) for i in input().split(' ')], reverse=True)

l_sum = 0
for k in range(K):
    l = ls[k]
    l_sum += l

print(l_sum)