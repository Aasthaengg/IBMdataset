n = int(input())
v = list(map(int,input().split()))
v.sort()
max = v[0]
for i in range(len(v)-1):
    max = (max + v[i+1])/2
print(max)


