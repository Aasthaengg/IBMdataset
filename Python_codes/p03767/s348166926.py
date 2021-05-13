N = int(input())
a = list(map(int,input().split()))

sort_a = sorted(a, reverse=True)

strong = 0
for i in range(N):
    strong += sort_a[2*i+1]

print(strong)