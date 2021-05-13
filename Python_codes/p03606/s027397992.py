n = int(input())
l, r = 0, 0
result = 0
for i in range(n):
    l, r = map(int, input().split())
    result = (r - l+1) + result
print(result) 