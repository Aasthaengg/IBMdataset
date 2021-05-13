n = int(input())
print(sum(len(str(i + 1)) % 2 for i in range(n)))