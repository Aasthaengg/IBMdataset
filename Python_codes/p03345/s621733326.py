A,B,C,K = map(int, input().split())

ans = B-A
if abs(ans) > 10**18:
    ans = "Unfair"
elif K%2 == 0:
    ans *= -1
print(ans)