a=int(input())
b=list(map(int,input().split()))
c=min(b)
d=0
b.pop(b.index(min(b)))
while True:
    if b==[]:
        break
    c+=min(b)
    b.pop(b.index(min(b)))
    d=c/2+d/2
    c=0
print(d)