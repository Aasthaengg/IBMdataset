N = int(input())
result = [n for n in range(N) if n % 2 == 0]
print(len(result) / N)