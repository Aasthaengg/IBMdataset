n = int(input())

*ab, = (tuple(map(int, input().split())) for _ in range(n))
x = max(ab, key=lambda x: x[0])
print(sum(x))
