N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))
 
diff = [V[i] - C[i] for i in range(N)]
diff.sort(reverse=True)
 
i, ans = 0,0
for d in diff:
    if d <= 0:
        break
    ans += d
print(ans)