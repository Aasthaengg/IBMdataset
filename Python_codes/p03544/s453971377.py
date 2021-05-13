n = int(input())

lucas = [2, 1]
for _ in range(n - 1):
    lucas.append(sum(lucas[-2:]))
else:
    print(lucas[-1])