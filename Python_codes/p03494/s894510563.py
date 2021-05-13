N = input()
A = [int(x) for x in input().split()]
def cnt(x):
    i = 0
    while x%2 == 0:
        x //= 2
        i += 1
    return i
ans = min(cnt(a) for a in A)
print(ans)