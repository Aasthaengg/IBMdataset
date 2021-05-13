n=int(input())
a=10*5
def k(n):
    s=tuple(map(int,tuple(str(n))))
    return sum(s)

for i in range(1,n):
    s=k(i)+k(n-i)
    if a>s:
        a=s
print(a)