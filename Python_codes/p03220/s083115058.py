N = int(input())
T,A = map(int,input().split())
H = list(map(int,input().split()))


ans = -1
diff = float('inf')
for i in range(N):
    d = abs(1000*T-6*H[i]-1000*A)

    if d < diff:
        diff = d
        ans = i + 1
print(ans)