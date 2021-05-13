N = int(input())
from math import sqrt
#N mod K = 0 or 1 となるk をさがす
#K = Nの約数　or N-1 の約数
def divisor(num):
    max_num = int(sqrt(num))
    divisor_list = []
    for i in range(1, max_num + 1):
        if num % i == 0:
            if i != 1:
                divisor_list.append(i)
            if num // i != 1:
                divisor_list.append(num//i)
    #sorted_divisor_list = sorted(divisor_list)
    return divisor_list

K_1 = divisor(N-1)
K_2 = divisor(N)
K_3 = []
count = 0
for k in K_2:
    temp = N
    while temp % k == 0:
        temp //= k
    if temp == 1 or temp % k == 1:
        count += 1
        K_3.append(k)
kk = K_1 + K_3
ans = len(set(kk))
print(ans)