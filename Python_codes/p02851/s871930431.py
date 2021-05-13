def main():
   n,k = map(int,input().split())
   a = list(map(int,input().split()))


   if k == 1:
      res = 0
      print(res)
   elif k == 2:
      res = 0
      for e in a:
         if e%k == 1:
            res += 1
      print(res)
   else:
      for i in range(n):
         a[i] = (a[i]-1)%k
      b = [0]
      d = {}
      d[0] = 1

      res = 0
      p = 0

      for i,e in enumerate(a):
         p = (p+e)%k
         if p in d:
            res += d[p]
            d[p] += 1
         else:
            d[p] = 1
         b.append(p)
         if i >= k-2:
            d[b[i-(k-2)]] -= 1
      print(res)

if __name__ == '__main__':
      main()


