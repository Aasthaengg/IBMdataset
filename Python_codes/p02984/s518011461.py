from collections import defaultdict as dd

n = int(input())
A = list(map(int, input().split()))
odd_ac = dd(int)
even_ac = dd(int)
for i, a in enumerate(A):
    if i % 2 == 0:
        even_ac[i] = even_ac[i-2] + a
    else:
        odd_ac[i] = odd_ac[i-2] + a
#print(odd_ac)
#print(even_ac)

ans = []
for dam in range(n):
    is_odd = dam % 2
    total = 0
    if is_odd:
        total += odd_ac[n-2] - odd_ac[dam-2]
        total -= even_ac[n-1] - even_ac[dam-1]
        total += even_ac[dam-1]
        total -= odd_ac[dam-2]
    else:
        total += even_ac[n-1] - even_ac[dam-2]
        total -= odd_ac[n-2] - odd_ac[dam-1]
        total -= even_ac[dam-2]
        total += odd_ac[dam-1]

    ans.append(total)

print(*ans, sep=" ")