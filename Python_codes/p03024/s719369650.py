import sys
input = sys.stdin.readline

S = list(input().strip())

m = {
    "o": 0,
    "x": 0,
}

for v in S:
    m[v] += 1
    
if m["x"] < 8:
    print("YES")
else:
    print("NO")