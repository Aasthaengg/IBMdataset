n, x = map(int, input().split())
m = [int(input()) for i in range(n)]
m = sorted(m)
num = int((x - (sum(m[1:n])))/ m[0])
print(num + len(m[1:n]))