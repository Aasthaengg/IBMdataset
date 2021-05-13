N,X=map(int, input().split())

m = [int(input()) for i in range(N)]

for i in range(len(m)):
    X-=m[i]
    
les=min(m)

print(len(m)+X//les)