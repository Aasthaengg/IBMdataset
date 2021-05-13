a, b, c = map(int, input().split())
tmp = [c % i == 0 for i in range(a, b+1)]
print(sum(map(int, tmp)))
