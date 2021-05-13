k = int(input())
d,f = k//50,k%50
n = 50
flow = [50-f-1]*(50-f) + [50-f+50]*f
base = [d]*50
print(n)
for i in range(50):
    print(base[i]+flow[i],end=" ")
print("")
