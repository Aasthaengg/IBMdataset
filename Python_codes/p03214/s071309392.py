n = int(input())
a = list(map(int, input().split()))
mean = sum(a) / len(a)
dstnc = [abs(i - mean) for i in a]
print(dstnc.index(min(dstnc)))
