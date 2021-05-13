import math

N, A, B = map(int, input().split())
V = list(map(int, input().split()))

# print(N, A, B, V)

V.sort(reverse=True)

max_list = V[:A]
max_sum = sum(max_list)
print(max_sum / A)

replace = max_list[-1]

num_replace = 0
for v in V:
    if v == replace:
        num_replace += 1

if num_replace == 1:
    print(1)
    exit()

num_replace_in_list = 0
for v in max_list:
    if v == replace:
        num_replace_in_list += 1

if replace * A != max_sum:
    ans = math.factorial(num_replace) // (math.factorial(num_replace - num_replace_in_list) * math.factorial(num_replace_in_list))
    print(ans)
    exit()


ans = 0
for i in range(A, B + 1):
    if i > num_replace:
        break
    ans += math.factorial(num_replace) // (math.factorial(num_replace - i) * math.factorial(i))

print(ans)
