n = int(input())
h,e = 0,n-1
print(0)
g = input()

while g != 'Vacant':
    mid = (h+e)//2
    print(mid)
    s = input()
    if s=='Vacant':exit()
    if g==s and mid%2==0 or g!=s and mid%2==1:
        h = mid + 1
    else:
        e = mid - 1
