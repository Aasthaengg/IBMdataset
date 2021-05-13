N,A,B = (int(x) for x in input().split())
X_arr = [int(x) for x in input().split()]

ans = 0
for i in range(N-1):
    ans += min(A*(X_arr[i+1]-X_arr[i]), B)

print(ans)


