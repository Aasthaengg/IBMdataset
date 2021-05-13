def sep():
    return map(int,input().strip().split(" "))
def lis():
    return list(sep())


n=int(input())
ar=lis()
if 0 in ar:
    print(0)
    quit()
p=1
for i in range(n):
    p*=ar[i]
    if p>10**18:
        print(-1)
        quit()
print(p)