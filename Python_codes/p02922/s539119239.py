A,B = map(int, input().split())
ans=1
if B==1:
    print(0)
    exit()
if A>=B:
    print(1)
    exit()

for i in range(1,10000):
    ans+=1
    if A+A*i-i>=B:
        print(ans)
        exit()

