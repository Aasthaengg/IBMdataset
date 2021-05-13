n = int(input())
a = list(map(int, input().split()))
av = sum(a) / n
aa = list(map(lambda x: abs(x - av), a))
aa = list(zip(aa, range(n)))
aa.sort()
print(aa[0][1])