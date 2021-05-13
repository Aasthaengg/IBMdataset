N = int(input())
A = list(map(int, input().split()))
height = 0
res = 0
for i in A:
    if i > height:
        height = i
    elif i < height:
        res += height - i
print(res)