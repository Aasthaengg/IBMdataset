import sys
input = sys.stdin.readline

n = int(input())
H = []
for i in range(n):
    a,b = input().split()
    H += [[int(a)+int(b),int(a),int(b)]]
H.sort(reverse=True)
ans = 0
for i in range(n):
    if i%2 == 0:
        ans += H[i][1]
    else:
        ans -= H[i][2]
print(ans)