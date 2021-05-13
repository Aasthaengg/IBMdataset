N = int(input())
a = list(map(int,input().split()))
a.sort()
b = a[N:]
print(sum(b[::2]))