# AtCoder
N = int(input())
A = list(map(int, input().split()))

ans = 0
s = 0
m = float('inf')

for i in A:
    i = abs(i)
    s += i
    m = min(m, i)

minus_num = len(list(filter(lambda x: x < 0, A)))

if minus_num % 2 == 0:
    print(s)
else:
    print(s-2*m)
