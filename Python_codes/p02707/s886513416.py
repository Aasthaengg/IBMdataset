N = int(input())
A = list(map(int,input().split()))

d = {}

for a in A :
    d.setdefault(a,0)
    d[a] += 1

# print(d)
for i in range(N) :
    if i+1 in d :
        print(d[i+1])
    else :
        print(0)