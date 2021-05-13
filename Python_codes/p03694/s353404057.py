N = int(input())
a= list(map(int, input().split()))
a = sorted(a)
print(abs(a[0] - a[-1]))