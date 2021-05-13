N = int(input())
l = [-1] * N

print(0)
s = input()
if s=="Male":
    l[0] = 0
elif s=="Female":
    l[0] = 1
else:
    exit(0)

print(N-1)
s = input()
if s=="Male":
    l[N-1] = 0
elif s=="Female":
    l[N-1] = 1
else:
    exit(0)

left, right = 0, N-1
while right-left>1:
    mid = (left+right)//2

    print(mid)
    s = input()
    if s=="Male":
        l[mid] = 0
    elif s=="Female":
        l[mid] = 1
    else:
        exit(0)

    if (l[mid]==l[left] and (mid-left)%2) or (l[mid]!=l[left] and (mid-left)%2==0):
        right = mid
    else:
        left = mid
