from copy import copy

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
b = copy(a)
b.reverse()

def count_more_x(x : int):
    j = 0
    ret = 0
    for i in range(len(b)):
        while j < len(a) and b[i]+a[j] < x:
            j += 1
        ret += j
    return n*n-ret

def sum_more_x(x : int):
    j = 0
    ret = 0
    for i in range(len(b)):
        while j < len(a) and b[i]+a[j] < x:
            j += 1
        ret += b[i]*(n-j)+c[j]
    return ret

lower = 0
upper = 1000000
while upper-lower > 1:
    middle = (upper+lower)//2
    if count_more_x(middle) < m:
        upper = middle
    else:
        lower = middle

left = lower

lower = 0
upper = 1000000
while upper-lower > 1:
    middle = (upper+lower)//2
    if count_more_x(middle) >= m:
        lower = middle
    else:
        upper = middle

right = upper

# print(left, right)
# print(count_more_x(right))
c = copy(a)
value = 0
for i in range(len(c)-1, -1, -1):
    value = value + c[i]
    c[i] = value
c.append(0)
ans = sum_more_x(right) + left*(m-count_more_x(right))
print(ans)

