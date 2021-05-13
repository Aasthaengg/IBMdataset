n = int(input())
a = list(map(int, input().split()))

def calc_sum(a, flag):
    ret = 0
    sum = 0
    for i in range(n):
        if (flag == 1 and sum + a[i] >= 0) or (flag == -1 and sum + a[i] <= 0):
            ret += abs(sum) + a[i] * flag + 1
            sum = -flag
        else:
            sum += a[i]
        flag = -flag
    return ret

print(min(calc_sum(a, 1), calc_sum(a, -1)))