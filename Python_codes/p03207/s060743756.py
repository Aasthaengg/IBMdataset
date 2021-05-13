n=int(input())
s=0
a=0
max=0
for i in range(n):
    p=int(input())
    if p>max:max=p
    a=max//2
    s=s+p
print(s-a)