n = int(input())
a = list(map(int,input().split()))

i = 1
ans = 1
change = [False,False]

while i<n:
    if change == [True,True]:
        ans += 1
        change = [False,False]
        #print(change)
    elif a[i]>a[i-1]:
        change[0] = True
        i += 1
        #print(change)
    elif a[i]<a[i-1]:
        change[1] = True
        i += 1
        #print(change)
    else:
        i += 1
        #print(change)
if i==n and change==[True,True]:
    ans += 1
print(ans)