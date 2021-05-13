k,s = map(int,input().split())
c=0
for i in range(k+1):
    for j in range(k+1):
         c += 1*(0 <= s - i -j <= k)
print(c)