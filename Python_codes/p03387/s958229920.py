l = sorted(map(int, input().split()))
p = (l[0]%2 != l[1]%2) or (l[1]%2 != l[2]%2)

p=(l[0]%2!=l[1]%2)or(l[1]%2!=l[2]%2)
l[0],l[1],l[2]=sorted([l[0]+((l[0]%2==l[1]%2)^(l[0]%2==l[2]%2)),l[1]+((l[1]%2==l[0]%2)^(l[1]%2==l[2]%2)),l[2]+((l[2]%2==l[0]%2)^(l[2]%2==l[1]%2))])
print((l[2]-l[0])//2+(l[2]-l[1])//2+p)