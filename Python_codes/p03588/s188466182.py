n = int(input())
max_ = 0
index_ = 0
for _ in range(n):
    a, b = map(int, input().split())
    if a > index_:
        index_ = a
        max_ = b
print(index_ + max_)