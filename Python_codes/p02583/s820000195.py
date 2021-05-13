N = int(input())
L = list(map(int, input().split()))

ans = 0
for x in L:
    for y in L:
        for z in L:
            if x != y:
                if x < z:
                    if y < z:
                        if x + y > z:
                            ans += 1

print(int(ans/2))
