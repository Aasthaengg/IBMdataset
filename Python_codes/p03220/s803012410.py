n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))
l = []
for i in range(n):
  l.append(abs(a-(t-h[i]*6/1000)))
print(l.index(min(l))+1)