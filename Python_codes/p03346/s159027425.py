n = int(input())

p = []
for _ in range(n):
    p.append(int(input()))
    
ans = [0 for _ in range(n + 1)]
for num in p:
    ans[num] = ans[num - 1] + 1
print(n - max(ans))