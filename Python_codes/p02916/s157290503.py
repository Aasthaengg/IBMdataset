n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

s = 0

for i in range(n):
    s += b[a[i]-1]
    if i > 0 and a[i-1] + 1 == a[i]:
        s += c[a[i-1]-1]

print(s)