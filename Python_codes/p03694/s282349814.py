N = int(input())
s = list(map(int, input().split()))
ans=max(s)-min(s)
print(ans)