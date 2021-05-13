A, B, C = list(map(int, input().split()))

ans = "Yes"

if ((A + B) < C):
    ans = "No"

print(ans)