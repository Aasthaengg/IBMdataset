n,q = map(int, input().split())  
a = input() 
l = [0]*n; 

for i in range(2,n+1):
    x = a[(i-2):i]
    l[i-1] = l[i-2]
    if x=='AC':
        l[i-1] += 1

for i in range(q):
  le,ri = map(int, input().split())  
  print(l[ri-1]-l[le-1]) 

