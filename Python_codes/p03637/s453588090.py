n = int(input())
al = list(map(int, input().split()))

foud = 0
twod = 0

for i in range(n):
    if al[i] % 4 ==0:
        foud += 1
    elif al[i] % 2 ==0:
        twod += 1
        
if (foud*2+1)+max(0,(twod-1)) >=n:
    print("Yes")
else:
    print("No")