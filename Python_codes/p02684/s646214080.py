n,k = map(int,input().split())
a = list(map(int,input().split()))

for i in range(n):
    a[i] -= 1
    
visited = [-1] * n
now = 0

for i in range(k):
    if visited[now] != -1:#訪れたことがあるか
        loop = i - visited[now]   #ループの大きさ
        k = (k-(i-loop)) % loop
        
        for _ in range(k):
            now = a[now]
        
        break
        
    visited[now] = i
    now = a[now] 
        
print(now + 1)