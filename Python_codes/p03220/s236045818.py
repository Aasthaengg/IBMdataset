N = int(input())
T,A = map(int,input().split())
H = list(map(int,input().split()))

ans = 1
tmpr_distA = abs(A - (T -0.006*H[0]))
for i in range(1,N,1):
    tmptmpr = abs(A - (T-0.006*H[i]))
    if tmptmpr < tmpr_distA:
        tmpr_distA = tmptmpr
        ans = i+1
print(ans)
