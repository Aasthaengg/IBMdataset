N = int(input())
d = sorted(map(int, input().split()))

index = len(d) // 2 - 1

ans = 0
if d[index] != d[index + 1]:
    ans = d[index + 1] - d[index]
    
print(ans)