N,X = map(int,input().split())
m = [int(input()) for _ in range(N)]
for i in m:
    X -= i
m.sort();
print(N+X//m[0])