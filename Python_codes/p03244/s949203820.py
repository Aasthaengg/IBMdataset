from collections import Counter

n = int(input())
a = list(map(int, input().split()))

a_even = [0] * (n//2); a_odd = [0] * (n//2)

for i in range(n):
    if i % 2 == 0:
        a_even[i//2] = a[i]
    else:
        a_odd[i//2] = a[i]

dic_even = Counter(a_even); dic_odd = Counter(a_odd)

first_even_key, first_even_num = max(dic_even.items(), key=lambda x: x[1])
dic_even.pop(first_even_key)
if len(dic_even) > 0:
    second_even_key, second_even_num = max(dic_even.items(), key=lambda x: x[1])
else:
    second_even_key = -1; second_even_num = 0

first_odd_key, first_odd_num = max(dic_odd.items(), key=lambda x: x[1])
dic_odd.pop(first_odd_key)
if len(dic_odd) > 0:
    second_odd_key, second_odd_num = max(dic_odd.items(), key=lambda x: x[1])
else:
    second_odd_key = -1; second_odd_num = 0

if first_even_key == first_odd_key:
    print(n - max(first_even_num + second_odd_num, second_even_num + first_odd_num))
else:
    print(n - first_even_num - first_odd_num)