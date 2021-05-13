n, m = map(int, input().split())

times = 2 ** m
print(1900*m*times + (n-m)*100*times)