s=int(input())
def col(n):
    if n%2==0:
        return n//2
    else:
        return 3*n+1
a=set()
a.add(s)
b=col(s)
count=2
while not b in a:
    a.add(b)
    b=col(b)
    count+=1
print(count)