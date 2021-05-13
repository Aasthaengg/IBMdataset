n = int(input())
a = list(map(int,input().split()))
ans = 0
while(any(a)):
    f = True
    x = a[0]
    for i,ai in enumerate(a):
        if ai:
            a[i] -= 1
        if ai < 1:
            if x != 0:
                break
        x = ai
    x = a[0]
    ans += 1
    #print(a)
print(ans)