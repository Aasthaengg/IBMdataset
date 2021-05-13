a = list(map(int, input().split()))
k = int(input())

am = max(a)
mp = a.index(am)

for i in range(k):
  am = am*2

a[mp] = am
print(sum(a))