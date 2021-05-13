N = int(input())
l = [-1] * N

def check(v):
    print(v)
    s = input()
    if s=="Male":
        l[v] = 0
    elif s=="Female":
        l[v] = 1
    else:
        exit(0)

check(0)
check(N-1)

left, right = 0, N-1
while right-left>1:
    mid = (left+right)//2
    check(mid)
    if (l[mid]==l[left] and (mid-left)%2) or (l[mid]!=l[left] and (mid-left)%2==0):
        right = mid
    else:
        left = mid
