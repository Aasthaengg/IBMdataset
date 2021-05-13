#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))


n = int(input())
p = list(map(int, input().split()))

q = sorted(p)

ans = 0
for i in range(n):
    if p[i] != q[i]:
        ans += 1
if (ans <= 2):
    print("YES")
else:
    print("NO")
