n = int(input())
a = list(map(int, input().split()))

def solve(l):
    if len(l) == 1:
        return l[0]

    min_l = min(l)
    ans = min_l
    new_l = []
    for i in l:
        i -= min_l
        if i == 0:
            if len(new_l) > 0:
                    ans += solve(new_l)
                    new_l = []
        else:
            new_l.append(i)
    if len(new_l) > 0:
        ans += solve(new_l)

    return ans

print(solve(a))