n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
m = 0
ans = 0
P = []
for a,b in zip(A,B):
    if a - b < 0:
        m += b-a
        ans += 1
    elif a - b > 0:
        P.append(a-b)
P.sort(reverse = True)
if m <= 0:
    print(ans)
else:
    for p in P:
        m -= p
        ans += 1
        if m <= 0:
            print(ans)
            break
    else:
        print(-1)
