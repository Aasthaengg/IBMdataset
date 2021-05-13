N=int(input())
a=100
def k(n):
    s=tuple(map(int,tuple(str(n))))
    return sum(s)
for i in range(1,N):
    s=k(i)+k(N-i)
    if s<a:
        a=s
print(a)