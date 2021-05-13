n = int(input())
t,a = map(int, input().split())
h = list(map(int, input().split()))
c = 0.006
for i in range(n):
    h[i] = abs(t - h[i] * c - a)
print(1 + h.index(min(h)))