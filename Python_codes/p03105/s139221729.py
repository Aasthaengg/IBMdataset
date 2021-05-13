#ABC-120-A
A, B, C = map(int, input().split())
ans = 0
while B >= A:
    B -= A
    ans += 1
    if ans == C:
        break
        
print(ans)