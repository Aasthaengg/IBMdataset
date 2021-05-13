n=int(input())
a=list(map(int,(input().split())))
l=1
a=sorted(a)
for i in range(n):
    l*=a[i]
    if l>10**18:
        print('-1')
        exit()
print(l)
