k,x = map(int,input().split())
t = []
for i in range(x-k+1,x+k):
    t.append(str(i))
print(' '.join(t))