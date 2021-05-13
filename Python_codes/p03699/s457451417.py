n=int(input())
a = [int(input()) for _ in range(n)]
a.sort()
for i in range(n):
    if sum(a)%10 == 0:
        if a[i]%10 == 0:
            continue
        else:
            a[i]=0
    else:
        print(sum(a))
        exit(0)
print(0)