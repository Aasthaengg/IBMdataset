n = int(input())
print(len(list(filter(lambda x : len(str(x)) % 2 & 1, range(1, n+1)))))
