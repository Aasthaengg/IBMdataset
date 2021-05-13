n = int(input())
#l, r = list(map(int, input().split()))
# A = list(map(int, input().split()))
a = list(map(int, input().split()))
# data = [list(map(int, input().split())) for i in range(n)]
# q = int(input())
#a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# ab_sorted = sorted(ab, key=lambda x: x[0])
#x = [list(map(int, input().split())) for i in range(n)]
# print(min(15*n, 100*(n//10+1), 100*(n//10)+15*(n % 10)))
# for i in range(1, int(n**0.5)+1):
total = sum(a)
s = 0
for i in range(1, n):
    if i % 2 != 0:
        s += a[i]
x = []
x.append(total - 2*s)
for i in range(1, n):
    x.append(2*a[i-1]-x[i-1])

for i in range(n):
    print(x[i], end=" ")
