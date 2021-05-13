n,x = map(int, input().split())
m = [int(input()) for _ in range(n)]
al = sum(m)
print(len(m)+(x-al)//min(m))