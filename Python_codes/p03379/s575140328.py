n = int(input())
x = list(map(int,input().split()))
X = sorted(x)
a = X[n//2]
b = X[n//2 -1]

for i in range(n):
     if x[i] >= a:
         print(b)
     elif x[i] <= b:
         print(a)  
         
