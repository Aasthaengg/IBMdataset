k = int(input())
a = list(map(int,input().split()))

l = 2
r = 2
for i in a[::-1]:
    if i > r:
        print(-1)
        exit()
    l = (l+i-1)//i*i
    r = r//i*i+i-1
    if r < l:
        print(-1)
        exit()
print(l,r)