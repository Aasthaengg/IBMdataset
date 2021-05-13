n = int(input())
a = list(map(int, input().split()))

a = sorted(a)
a = a[n:]

print(sum(a[0::2]))
