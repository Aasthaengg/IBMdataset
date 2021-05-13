n = int(input())
a = list(map(int, input().split()))
e=0
o=0
for i in range(n):
    if a[i]%2==0:
        e+=1
    else:
        o+=1
if n%2==0 and o%2==0:
    print("YES")
elif n%2!=0 and o%2==0:
    print("YES")
else:
    print("NO")