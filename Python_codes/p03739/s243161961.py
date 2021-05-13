n = int(input())
a = list(map(int, input().split()))


def calc(init):
    ans = 0
    sum = 0
    prev = init
    for i in range(n):
        sum += a[i]
        if sum == 0:
            ans += 1
            if prev < 0:
                sum = 1
            else:
                sum = -1
        else:
            if sum > 0 and prev > 0:
                ans += sum + 1
                sum = -1
            elif sum < 0 and prev < 0:
                ans += 1 - sum
                sum = 1
        prev = sum
    return ans


print(min(calc(1), calc(-1)))
