N = int(input())
ABs = []
sum_B = 0
for i in range(N):
    a,b = map(int, input().split())
    ABs.append(a+b)
    sum_B += b 
ABs.sort(reverse=True)
ans = sum(ABs[::2])-sum_B
print(ans)