# coding: utf-8

n = int(input().rstrip())

numbers = list(map(int, input().rstrip().split(" ")))

tmp = list(sorted([ [numbers[i] - i, i] for i in range(n)]))


ans = 1000000000 * n

target = tmp[int(n/2)][0]
if n % 2 == 0:
    target = int((tmp[int(n/2)][0]+tmp[int(n/2)-1][0])/2)

ans = [abs(numbers[i] - (target + i)) for i in range(n)]
print(sum(ans))
