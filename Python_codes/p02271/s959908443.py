def solve(i, m):
    if (i, m) in solved_dict:
        return solved_dict[(i, m)]
    if m == 0:
        return True
    if m < 0:
        return False
    if i >= n:
        return False
    solved_dict[(i, m)] = solve(i + 1, m - A[i]) or solve(i + 1, m)
    return solved_dict[(i, m)]

solved_dict = {}
n = int(input())
A = list(map(int, input().split()))
q = int(input())
for m in list(map(int, input().split())):
    print("yes" if solve(0, m) else "no")
