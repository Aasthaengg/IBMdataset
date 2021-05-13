n,m,c = map(int,input().split())
b = list(map(int,input().split()))

cnt = 0

for i in range(n):
    a = list(map(int,input().split()))
    ab = [x*y for x,y in zip(a,b)]
    if sum(ab) + c > 0:
        cnt += 1
        
print(cnt)