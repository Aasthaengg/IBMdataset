n = int(input())
l = 0
r = n-1
mid = (l+r)/2
print(l)
s1 = raw_input()
if s1 == 'Vacant':
    exit(0)
print(mid)
s2 = raw_input()
if s2 == 'Vacant':
    exit(0)
while True:
    #print("before:",l,r)
    if (mid-l) % 2 == int(s1 != s2):
        l = mid
        s1 = s2
    else:
        r = mid
    #print("after:",l,r)
    mid = (l+r)/2
    if mid == l:
        break
    print(mid)
    s2 = raw_input()
    if s2 == 'Vacant':
        exit(0)
print(mid+1)
s1 = raw_input()
