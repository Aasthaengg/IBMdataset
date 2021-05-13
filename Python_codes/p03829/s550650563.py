t = list(map(int, input().split()))
k = list(map(int, input().split()))

h = 0
for i in range(0,len(k)-1):
    if (k[i+1]-k[i])*t[1] > t[2]:
        h += t[2]
    else:
        h += (k[i+1]-k[i])*t[1]
print(h)