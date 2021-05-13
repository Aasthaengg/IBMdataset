import numpy as np

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    # divisors.sort()
    return divisors

n, k = map(int, input().split())
a = list(map(int, input().split()))

arr = np.array(a)
wa = sum(arr)
divisors = make_divisors(wa)

ans = 1
for div in divisors:
    lst = [0] * n
    for i in range(n):
        lst[i] = a[i] % div
    lst.sort()
    lst = [i for i in lst if i != 0]
    if lst == []:
        ans = max(ans, div)
    arr = np.array(lst)
    arr_amari = np.cumsum(arr)
    arr_reversed = arr[::-1]
    arr_husoku = np.cumsum(div - arr_reversed)[::-1]
    for i in range(len(arr_amari)-1):
        if arr_amari[i] == arr_husoku[i+1] and arr_amari[i] <= k:
            ans = max(ans, div)

print(ans)