a = list(map(int, input().split()))
a.sort()
b = [a[i+1]-a[i] for i in range(len(a)-1)]

print(sum(b))