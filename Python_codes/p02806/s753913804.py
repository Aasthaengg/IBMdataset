def solve(n, s, t, x):
    for i in range(n):
        if s[i] == x:
            return sum(t[i+1:])
    return 0

n = int(input())
s = [0] * n
t = [0] * n
for i in range(n):
    s[i], t[i] = input().split()
    t[i] = int(t[i])
x = input()
print(solve(n, s, t, x))