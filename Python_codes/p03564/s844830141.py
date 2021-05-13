n=int(input())
k=int(input())
a=1
for i in range(n):
    if a*2<a+k:a*=2
    else:a+=k
print(a)