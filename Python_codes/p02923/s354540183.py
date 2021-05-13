n = int(input())
h = list(map(int,input().split()))
b = [0]*(n-1)
for i in range(n-1):
    if h[i]-h[i+1]>=0:
        b[i]=1


c = (''.join(map(str, b))).split("0")
#print(c)
d = set(c)
#print(d)
print(len(max(d)))
