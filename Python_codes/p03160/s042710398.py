n = int(input())
h = list(map(int,input().split()))

c = []
c.append(0)
c.append(abs(h[1]-h[0]))


for i in range(2,n):
    c.append(min(c[i-2]+abs(h[i]-h[i-2]),c[i-1]+abs(h[i]-h[i-1])))


print(c[n-1])