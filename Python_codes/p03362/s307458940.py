N=int(input())
def eratosthenes(n):
    prime = [2]
    limit = int(n**0.5)
    data = [i + 1 for i in range(2, n, 2)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]
l=eratosthenes(55555)
cnt=0
for i in l:
   if i%5==1:
      print(i,end=" ")
      cnt+=1
   if cnt==N:
      exit()