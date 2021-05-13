n,k= map(int, input().split())
for i in range(21200000):
    i+=1
if k==1:
    print(0)
else:
    print(n-k)