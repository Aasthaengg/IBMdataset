n = int(input())
a = list(map(int,input().split()))

S = sum(a)
x = [0]*n
x[0] = S
for i in range(1,n-1,2):
    x[0] -= 2*a[i]

for j in range(1,n):
    x[j] = 2*a[j-1] - x[j-1]

lis = map(str,x)
#print(x)
print(" ".join(lis))    