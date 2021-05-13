r = int(input())
ans = 'ABC'
if r >= 1200:
    ans = 'ARC'
    if r >= 2800:
        ans = 'AGC'
print(ans)