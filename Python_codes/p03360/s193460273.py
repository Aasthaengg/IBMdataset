abc = list(map(int, input().split()))
k = int(input())

# print(abc)
# print(k)

# print(max(abc))
# print(abc.index(max(abc)))
max_index = abc.index(max(abc))

for _ in range(k):
    abc[max_index] = abc[max_index] * 2

# print(abc)
print(sum(abc))
