n=int(input())
a=2
b=1
for i in range(n-1):
    old_a=a
    a=b
    b=old_a+b
print(b)