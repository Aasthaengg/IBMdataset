n = int(input())
a = list(map(int,input().split()))
a = list(reversed(sorted(a)))
x = 0
y = 0
for i in range(len(a)-1):
         if a[i] == a[i+1]:
                  x = a[i]
                  break
for j in range(i+2,len(a)-1):
         if a[j] == a[j+1]:
                  y = a[j]
                  break
print(x*y)
