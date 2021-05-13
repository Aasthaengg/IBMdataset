n=int(input())
k=int(input())
a=1
for i in range(n):
    if a>k:
        a=a+k
    else:
        a=2*a
print(a)