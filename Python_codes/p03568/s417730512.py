N = int(input())
a = list(map(int, input().split()))
ans = 1
for i in range(N):
    if a[i] % 2 == 0:
       ans *= 2
if N != 1:
    print(3**N-ans)
else:
    if a[0] % 2 == 0:
        print(1)
    else:
        print(2)
