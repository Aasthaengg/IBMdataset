l = sorted(list(map(int,input().split())))

a = abs(l[0]-l[1])%2
b = abs(l[1]-l[2])%2
c = abs(l[0]-l[2])%2

if a==0:
    if b==0:
        ans = (l[2]-l[0] + l[2]-l[1]) /2
    else:
        ans = 1 + (l[2]-(l[0]+1) + l[2]-(l[1]+1))/2
else:
    if b==0:
        ans = 1 + ((l[2]+1)-l[0] + (l[2]+1)-(l[1]+1))/2
    else:
        ans = 1 + ((l[2]+1)-(l[0]+1) + (l[2]+1)-l[1])/2
print(int(ans))