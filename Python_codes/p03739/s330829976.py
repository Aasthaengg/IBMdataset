n = int(input())
a = list(map(int, input().split()))
 
r_even = 0  # 偶数桁を＋にする場合の値
a_even = a[:]
sum_even = 0
for i in range(len(a)):
    sum_even += a_even[i]
    if i % 2 == 0:
        if sum_even <= 0:
            r_even += 1 - sum_even
            a_even[i] += 1 - sum_even
            sum_even += 1 - sum_even
    else:
        if sum_even >= 0:
            r_even += sum_even + 1
            a_even[i] -= sum_even + 1
            sum_even -= sum_even + 1

r_odd = 0   #奇数桁を＋にする場合の値
a_odd = a[:]
sum_odd = 0
for i in range(len(a)):
    sum_odd += a_odd[i]
    if i % 2 != 0:
        if sum_odd <= 0:
            r_odd += 1 - sum_odd
            a_odd[i] += 1 - sum_odd
            sum_odd += 1 - sum_odd
    else:
         if sum_odd >= 0:
            r_odd += sum_odd + 1
            a_odd[i] -= sum_odd + 1
            sum_odd -= sum_odd + 1

print(min(r_odd, r_even))
