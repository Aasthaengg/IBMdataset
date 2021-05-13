N=int(input())
l=[tuple(map(int, input().split())) for i in range(N)]
t=0
for i in l[::-1]:
    t+=i[1]-(i[0]+t-1)%i[1]-1
print(t)