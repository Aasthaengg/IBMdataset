N = int(input())
h = list(map(int, input().split()))
l = list(map(int, input().split()))
c = 0

for i in range(N):
    c = max(sum(h[0:i+1])+sum(l[i:N+1]), c)

print(c)