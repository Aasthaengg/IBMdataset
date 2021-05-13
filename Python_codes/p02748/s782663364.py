if __name__ == '__main__':
   a, b, n = map(int, input().split())
   lista =  [int(i) for i in input().split()]
   listb =  [int(i) for i in input().split()]
   minP = min(lista) + min(listb)

   for i in range(n):
       c = [int(i) for i in input().split()]
       now =lista[c[0]-1] + listb[c[1]-1] - c[2]
       if  now< minP :
           minP=now

   print(minP)