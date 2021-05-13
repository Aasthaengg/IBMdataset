N = int(input())
p = list(map(int, input().split()))
result = 0
piyo = False
for i in range(N):
    if i + 1 == p[i] and not piyo:
        result += 1
        piyo = True
    else:
        piyo = False
print(result)