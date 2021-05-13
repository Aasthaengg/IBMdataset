n = int(input())
b = list(map(int,input().split()))
ans = sum([min(b[i],b[i+1]) for i in range(n-2)])
ans += b[0] + b[n-2]
print(ans)