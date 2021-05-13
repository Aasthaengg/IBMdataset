n = int(input())
a = list(map(int, input().split()))

l = list(map(lambda x: abs(x-sum(a)/n) ,a))
print(l.index(min(l)))