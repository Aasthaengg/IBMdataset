#ABC 142 B
N,K = map(int,input().split())
H = [int(h) for h in input().split()]
H = sorted(H)
import bisect
ans =len(H)-bisect.bisect_left(H,K)
print(ans)