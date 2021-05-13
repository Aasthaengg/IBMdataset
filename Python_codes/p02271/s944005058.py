n = int(input())
a = list(map(int, input().split()))
# count on j
# 最初に入力したリスト

q = int(input())
m = list(map(int, input().split()))
# count on i
# 後に入力したリスト


def solve(i, m_count):
    if m_count == 0:
        return True
    if i >= n:
        return False
    res = solve(i + 1, m_count) or solve(i + 1, m_count - a[i])
    return res


for count in m:
    if sum(a) < count:
        print("no")
    elif solve(0, count):
        print("yes")
    else:
        print("no")

