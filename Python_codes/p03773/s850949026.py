A,B = list(map(int,input().split()))
ans = A + B
if ans >= 24:
    ans -= 24
print(ans)