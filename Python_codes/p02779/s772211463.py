n = int(input())
s = list(map(int, input().split()))

st = set(s)

if len(st) == n:
    print("YES")
else:
    print("NO")
