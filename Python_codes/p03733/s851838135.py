n,t = map(int, input().split())
tl = list(map(int,input().split()))
c = 0
for i  in range(n-1):
    if tl[i] + t <= tl[i+1]:
        c += t
    else:
        c += tl[i+1]-tl[i]
print(c+t)