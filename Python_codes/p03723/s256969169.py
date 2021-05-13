A, B, C = list(map(int, input().split()))
[A, B, C].sort() #smaller~bigger
if A==B and B==C:
    if A%2==0:
        print(-1)
    else:
        print(0)
elif (A%2==1) or (B%2==1) or (C%2==1):
    print(0)
else:
    cnt = 0
    while ((A%2==0) and (B%2==0) and (C%2==0)):
        [A, B, C] = [(A+B)/2, (A+C)/2, (B+C)/2]
        cnt += 1
    print(cnt)
