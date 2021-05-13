n = int(input())
a = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

def test(i, s, target):
    if s == target:
        return 1
    if s > target or i == n:
        return 0
    if s + sum(a[i:]) < target:
        return 0

    return test(i+1, s, target) or test(i+1, s+a[i], target)

for target in m:
    ans = 'yes' if test(0, 0, target) else 'no'
    print(ans)
