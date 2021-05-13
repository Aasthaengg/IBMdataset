from sys import stdin

n, m = [int(x) for x in stdin.readline().rstrip().split()]
a = [int(x) for x in stdin.readline().rstrip().split()]

lb = -1
ub = 1e+09 + 3
total_money = sum(a)

while ub - lb > 1:
    mid = (lb + ub) // 2
    count = 0
    ac = a[:]
    for i in range(len(ac)):
        while ac[i] > mid:
            if ac[i] == 0:
                break
            ac[i] //= 2
            count += 1
        if count > m:
            break
    if count > m:
        lb = mid
    else:
        ub = mid
        ac.sort(reverse=True)
        if count < m:
            for i in range(m-count):
                if i >= n:
                    break
                ac[i] //= 2
        total_money = sum(ac)


print(total_money)