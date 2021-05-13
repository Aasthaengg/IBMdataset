l = list(map(int,input().split()))
N = l[0]
Y = l[1]

l = list()

for i in range(N+1):
    a = i
    if (Y - 1000*N -9000*a) % 4000 == 0:
        b = (Y - 1000*N -9000*a) // 4000 
        c = N - a - b
        if a >= 0 and b >= 0 and c >= 0:
            l.append([a,b,c])
            break

if len(l) ==0:
    print("-1 -1 -1")
else:
    ans = l[0]
    print(ans[0],ans[1],ans[2])