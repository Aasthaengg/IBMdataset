N = int(input())
CONST = 10 ** 18
result = 1
numbers = list(map(int, input().split()))
if 0 in numbers:
    print(0)
    exit(0)
numbers.sort(reverse=True)
for i in numbers:
    result = result * i
    if result > CONST:
        print(-1)
        exit(0)
print(result)