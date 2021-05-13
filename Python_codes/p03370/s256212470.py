n,x = list(map(int,input().split()))
m = [int(input()) for i in range(n)]

m.sort()
n_x = x-sum(m)
cnt = n
while n_x>=m[0]:
    n_x-=m[0]
    cnt+=1

print(cnt)
