abc = list(map(int, input().split()))
x = max(abc)
abc.remove(x)
print(sum(abc))
