n = int(input())
dlst = list(map(int, input().split()))
m = int(input())
tlst = list(map(int, input().split()))

dlst.sort()
tlst.sort()
posd = 0
post = 0

while 1:
    if dlst[posd] == tlst[post]:
        posd += 1
        post += 1
    else:
        posd += 1
    if post == m:
        print("YES")
        exit()
    elif posd == n:
        print("NO")
        exit()