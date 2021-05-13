n = int(input())
a = list(map(int, input().split()))
a = list(reversed(sorted(a)))
print(sum(a[1::2][:n]))