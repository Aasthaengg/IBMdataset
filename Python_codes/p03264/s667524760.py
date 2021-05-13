K = int(input())

odd = [0 for i in range(1, K + 1) if i % 2 == 1]
even = [0 for i in range(1, K + 1) if i % 2 == 0]

print(len(odd) * len(even))
