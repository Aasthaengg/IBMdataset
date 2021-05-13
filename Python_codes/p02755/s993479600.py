

A,B = list(map(int, input().split()))
ans = 10e7
is_true = False
for i in range(1,1010):
    a = int(i*0.08)
    b = int(i*0.10)
    if a == A and b == B:
        ans = min(ans, i)
        is_true = True
if is_true:
    print(ans)
else:
    print(-1)

