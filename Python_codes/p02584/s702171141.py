X, K, D = map(int, input().split())

def sign(x):
    return 1 if x >= 0 else -1


ans = abs(X) - K * D

if abs(X) - K * D < 0:
    divs = abs(X) // D
    mods = abs(X) % D
    nums = K - divs

    ans = abs(mods - (nums%2) * D)

print(ans)


# ans = min([abs(X+D*i) for i in range(-K, K+1, 2)])
# 
# print(ans)
