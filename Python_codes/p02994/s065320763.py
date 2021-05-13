n, l = list(map(int, input().split()))
left = l
right = l + n - 1
eat = 0
if left >= 0:
    eat = left
elif right <= 0:
    eat = right
t = 0
for i in range(n):
    t += i + l
print(t - eat)
