def average(x,y):
    return (x+y)/2
N=int(input())
v=list(map(int,input().split()))
v.sort()
for i in range(N-1):
    v[i+1]=average(v[i],v[i+1])
print(v[N-1])