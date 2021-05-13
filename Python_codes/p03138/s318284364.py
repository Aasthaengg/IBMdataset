n, k = [int(x) for x in input().split()]
a_list = [int(x) for x in input().split()]
s=0
l = len(bin(k)) - 2
b = n / 2
x = 0
for i in range(l, -1, -1):
    count = sum([(a >> i) & 1 for a in a_list])
    if count < b:
        temp = 1 << i
        if x + temp <= k:
            x += temp
print(sum([x ^ a for a in a_list]))
