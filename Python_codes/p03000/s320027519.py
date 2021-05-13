N,X=map(int,input().split())
l=list(map(int,input().split()))

count = 1

d = 0

for x  in l:
    d = d + x

    if d <= X:
        count += 1

print(count)