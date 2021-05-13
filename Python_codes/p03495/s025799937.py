n, k = map(int, input().split())
a = list(map(int, input().split()))
l = [0] * n
count = 0
for i in a:
        l[i-1] += 1
l.sort(reverse = True)
for i in range(k):
    count += l[i]
print(n-count)