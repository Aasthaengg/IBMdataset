n, k  = map(int,input().split())
l = list(map(int,input().split()))
result = 0
numbers = []
sorted_A = sorted(l,reverse=True)
for i in range(k):
    result += sorted_A[i]
print(result)