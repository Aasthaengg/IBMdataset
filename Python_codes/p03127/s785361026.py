def solve(a, b):
    mod = b%a
    if mod == 0:
        return a
    else:
        return solve(mod, a)

N = int(input())
A = list(map(int, input().split()))

minA = min(A)
B = [a%minA for a in A]
print(solve(minA, max(B)))