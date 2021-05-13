N = int(input())
a = list(map(int,input().split()))

a.sort(reverse=True)
s = 0

for i in [n*2-1 for n in range(1,N +1)]:
    s += a[i]

print(s)
