k=int(input())
a=list(map(int,input().split()))
l=2
h=2
for i in a[::-1]:
    tl=i*-(-l//i)
    th=i*(h//i)
    if tl>h or th<l:
        print(-1)
        quit()
    else:
        l=tl
        h=th+i-1
print(l,h)