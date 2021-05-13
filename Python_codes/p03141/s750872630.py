n,*ab = map(int,open(0).read().split())
abc = [(ab[i*2],ab[i*2+1],ab[i*2]+ab[i*2+1]) for i in range(n)]
abc.sort(key=lambda x:x[2],reverse = True)
print(sum([abc[i][0] if i%2==0 else -abc[i][1] for i in range(n)]))