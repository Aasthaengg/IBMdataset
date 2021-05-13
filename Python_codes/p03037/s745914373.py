n, m = map(int,input().split())
start = 1
end = n
for i in range(m):
    x, y = map(int,input().split())
    start = max(start, x)
    end = min(end, y)
print(end-start+1 if end-start >=0 else 0)
