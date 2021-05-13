w,a,b = list(map(int,input().split()))

ans = b-(a+w) if a <= b else a-(b+w)
print(ans if ans >= 0 else 0)
