X = int(input())

lst = [ [400, 599, 8], [600, 799, 7], [800, 999, 6], [1000, 1199, 5], [1200, 1399, 4], [1400, 1599, 3], [1600, 1799, 2], [1800, 1999, 1] ]

def Kyu(X):
   
   for i in lst:
      if i[0] <= X <= i[1]:
         result = i[2]
         break
   print(result)

Kyu(X)