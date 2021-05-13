n=int(input())
a=input()
b=[]

for i in range(n-2):
  b.append(a[i]+a[i+1]+a[i+2])
  
print(b.count('ABC'))