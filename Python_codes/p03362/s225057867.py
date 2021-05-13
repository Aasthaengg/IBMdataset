import sys
input = sys.stdin.readline
INF = 10**9
MOD = 10**9 + 7

def sieve(n):
    prime=[]
    limit=n**0.5
    data=[i+1 for i in range(1,n)]
    while True:
        p=data[0]
        if limit<=p:
            return prime+data
        prime.append(p)
        data=[e for e in data if e%p!=0]
   
primes = sieve(55556)

def main():
   n = int(input())
   
   ans = []
   for p in primes:
      if p%5 == 1:
         ans.append(p)
         if len(ans) == n:
            break
   
   print(*ans)
   
if __name__=='__main__':
    main()