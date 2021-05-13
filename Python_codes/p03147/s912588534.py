N = int(input())
h = list(map(int,input().split()))

counter = 0
while 1:
    if max(h)==0:
        break
    i = 0
    while i < N:
        if h[i] > 0:
            counter += 1
            while i<N and h[i] > 0:
                h[i]-=1
                i+=1
        else:
            i+=1
print(counter)
