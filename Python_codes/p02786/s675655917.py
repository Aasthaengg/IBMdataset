H = int(input())

def f(H):
    ans = 0
    if H > 1:
        ans += 2*f(H//2)+1
    else:
        return 1
    return ans

ans = f(H)
print(ans)