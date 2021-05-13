N = int(input())
m = list(map(int,input().split()))
m = sorted(m,reverse=True)

ans = sum(m[::2])-sum(m[1::2])
print(ans)