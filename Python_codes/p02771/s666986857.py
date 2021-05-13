import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().split())
inl = lambda: list(map(int, input().split()))
 
a, b, c = inm()
ans = False
if a == b and b != c:
    ans = True
if a == c and c != b:
    ans = True
if b == c and c != a:
    ans = True
print("Yes" if ans else "No")