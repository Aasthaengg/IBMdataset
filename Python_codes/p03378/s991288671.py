n, m, x = map(int, input().split())
a_list = list(map(int, input().split()))

# print(f"{n} {m} {x}")
# print(a_list)

n_list = [0] * (n + 1)
# print(n_list)

n_list[x] = 'X'
for i in range(m):
    n_list[a_list[i]] = 1
# print(n_list)

# print(n_list[:x])
# print(n_list[x + 1:])
print(min(sum(n_list[:x]), sum(n_list[x + 1:])))