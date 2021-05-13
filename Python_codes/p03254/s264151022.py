N, x = map(int,input().split())
a = sorted([int(i) for i in input().split()])
count = 0
if sum(a) == x:
    print(len(a))
else:
    for i in a:
        x = x-i
        if x<0:
            break
        count+=1
    if count == N:
        print(N-1)
    else:
        print(count)