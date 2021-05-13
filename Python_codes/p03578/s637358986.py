n=int(input())
d=list(map(int,input().split()))
m=int(input())
t=list(map(int,input().split()))

d.sort(reverse=True)
t.sort(reverse=True)

for i in range(n):
    if t[-1]==d[-1]:
        d.pop()
        t.pop()
    else:
        d.pop()
    if t==[]:
        print("YES")
        exit()
    if d==[]:
        print("NO")
        exit()