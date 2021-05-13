import math

n = int(input())
end = math.ceil((-1 + (1 + 8 * n)**(0.5)) / 2)

ans = [j for j in range(1, end+1)]

sum_to_end = ( end ** 2 + end ) // 2

if sum_to_end != n:
    ans.remove(sum_to_end - n)

print('\n'.join(map(str, ans)))