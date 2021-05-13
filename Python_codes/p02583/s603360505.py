N =int(input())
L=list(map(int, input().split()))
LL = sorted(L)
count=0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if LL[i]+LL[j]>LL[k]:
                if (LL[i]!=LL[j])and(LL[j]!=LL[k]):
                    count += 1
print(count)