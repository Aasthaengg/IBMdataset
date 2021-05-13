N = int(input())
t = list(map(int, input().split()))
M = int(input())
ans = sum(t)
for i in range(M):
    a, b = map(int, input().split())
    print(ans-t[a-1]+b)
    
