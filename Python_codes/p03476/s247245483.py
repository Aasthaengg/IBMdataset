Q=int(input())
l=[0]*100001
l2=[0]*100001
def d(n):
    prime = [2]
    limit = int(n**0.5)
    data = [i + 1 for i in range(2, n, 2)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]
for i in d(100000):
   l[i]=1
for i in range(3,100001):
   if l[i] == 1:
      if l[(i+1)//2]==1:
         l2[i]=1
for i in range(1,100001):
   l2[i]+=l2[i-1]
qe=[list(map(int,input().split())) for i in range(Q)]
for i in qe:
   print(l2[i[1]]-l2[i[0]-1])