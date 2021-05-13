import math

N, A, B = map(int, input().split())
V = list(map(int, input().split()))

# print(N, A, B, V)

V.sort(reverse=True)

max_list = V[:A]
max_sum = sum(max_list)
print(max_sum / A)

replace = max_list[-1]

num_replace = V.count(replace)

if num_replace == 1:
    print(1)
    exit()

num_replace_in_list = max_list.count(replace)

def combinations(n, m):
    return math.factorial(n) // (math.factorial(n - m) * math.factorial(m))

if replace * A != max_sum:
    ans = combinations(num_replace, num_replace_in_list)
    print(ans)
    exit()


ans = 0
for i in range(A, B + 1):
    if i > num_replace:
        break
    ans += combinations(num_replace, i)

print(ans)
