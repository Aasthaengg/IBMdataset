import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

n = ini()
a = inl()
j = 1
for i in range(n):
    a[i] -= j
    j += 1
a = sorted(a)
x = a[n//2]
ans = 0
for i in range(n):
    ans += abs(a[i] - x)
print(ans)