n = int(input())
ls = list(map(int,input().split()))
new = sorted(ls)
for i in ls:
    if i < new[int(n/2)]:
        print(new[int(n/2)])
    else:
        print(new[int(n/2)-1])
