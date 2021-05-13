N,T = map(int,input().split())
A = list(map(int,input().split()))

now = 0
end = 0
ans = 0
for i in range(N):
    a = A[i]
    ans += min((T-(end-a)),T)
    now = a
    end = a+T
print(ans)