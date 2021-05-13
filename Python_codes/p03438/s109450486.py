N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

diff = [a[i] - b[i] for i in range(N)]
plus = sum(filter(lambda x: x > 0, diff))
minus_even = sum(filter(lambda x: x < 0 and x % 2 == 0, diff))
minus_odd = sum(x + 1 for x in diff if x < 0 and x % 2 == 1)

# print(plus)

if plus * 2 + minus_even + minus_odd > 0:
    print('No')
else:
    print('Yes')