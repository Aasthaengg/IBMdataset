n=int(input())
k=int(input())
l=1
for i in range(n):
    if l<=k:l*=2
    else:l+=k
print(l)