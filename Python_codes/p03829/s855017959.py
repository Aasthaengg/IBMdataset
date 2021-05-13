N,A,B = map(int,input().split())
Data = list(map(int,input().split()))
ans = 0
for i in range(len(Data)-1):
    d = Data[i+1]-Data[i]
    ans += min(A*d,B)
print(ans)
