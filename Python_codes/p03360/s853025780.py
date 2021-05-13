n = list(map(int,input().split()))
k = int(input())
n.sort()
for i in range(k):
    n[2] *= 2
print(sum(n))