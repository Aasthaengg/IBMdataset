a,b = map(int, open(0).read().split())

print(sum(str(i) == str(i)[::-1] for i in range(a,b+1)))