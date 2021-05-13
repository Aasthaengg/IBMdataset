n = int(input())
a = list(map(int, input().split()))
ave = sum(a) / n
aa = [abs(i - ave) for i in a]
print(aa.index(min(aa)))