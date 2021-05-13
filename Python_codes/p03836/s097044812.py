def solve():
    sx, sy, tx, ty = map(int, input().split())
    ans = ''
    ans += (ty - sy) * 'U'
    ans += (tx - sx) * 'R'
    ans += (ty - sy) * 'D'
    ans += (tx - sx) * 'L'
    ans += 'L'
    ans += (ty - sy + 1) * 'U'
    ans += (tx - sx + 1) * 'R'
    ans += 'D'
    ans += 'R'
    ans += (ty - sy + 1) * 'D'
    ans += (tx - sx + 1) * 'L'
    ans += 'U'
    return ans

print(solve())