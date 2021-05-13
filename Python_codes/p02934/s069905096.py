N = int(input())
array = list(map(int, input().split()))

print(
    1 / sum(1/A for A in array)
)