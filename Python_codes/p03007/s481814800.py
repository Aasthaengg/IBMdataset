N = int(input())
l = list(map(int,input().split()))
l.sort()
sousa = []
next_m = l[0]
next_p = l[N-1]
for i in range(1,N-1):
    if l[i] > 0:
        sousa.append([next_m,l[i]])
        next_m -= l[i]
    else:
        sousa.append([next_p,l[i]])
        next_p -= l[i]
ans = next_p - next_m
print(ans)
sousa.append([next_p,next_m])
for i in range(N-1):
    print(str(sousa[i][0])+" "+str(sousa[i][1]))

