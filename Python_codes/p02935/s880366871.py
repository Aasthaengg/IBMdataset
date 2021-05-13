N = int(input())
v = list(map(int, input().split()))

v.sort()

result = 0
for i in range(N-1):
    if i == 0:
        result = v[i]
        result = (result + v[i+1]) / 2
    else:
        result = (result + v[i+1]) / 2
    

print(result)