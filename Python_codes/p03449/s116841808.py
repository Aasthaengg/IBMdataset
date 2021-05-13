n = int(input())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
start = a1[0]
result = []
for i in range(n):
    aa = i+1
    result.append(sum(a1[:n-i]) + sum(a2[n-aa:]))
print(max(result))