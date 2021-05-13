x,n = map(int,input().split())
p = list(map(int,input().split()))
p.sort()
right = x
left = x
while True:
    if left in p:
        left -= 1
    else:
        print(left)
        break
    if right in p:
        right += 1
    else:
        print(right)
        break