n = int(input())
a_ls = list(map(int, input().split()))
num_mul4 = 0
num_even_not4 = 0
num_odd = 0
for i in range(n):
    if a_ls[i] % 4 == 0:
        num_mul4 += 1
    elif a_ls[i] % 2 == 0:
        num_even_not4 += 1
    else:
        num_odd += 1
res = 'No'
if num_even_not4 == 0:
    if num_odd <= num_mul4 + 1:
        res = 'Yes'
else:
    num_odd += 1
    if num_odd <= num_mul4 + 1:
        res = 'Yes'
print(res)