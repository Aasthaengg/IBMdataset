N,A,B = map(int,input().split())
MAX = min(A,B)
MIN = max(A+B-N,0)
ans = [MAX,MIN]
print(*ans)