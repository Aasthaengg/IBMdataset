N = int(input())
A = [int(i) for i in input().split()]
A.append(0)
ary = []
for i, a in enumerate(A):
    if i == 0:
        ary.append(abs(0-a))
    else:
        ary.append(ary[-1]+abs(A[i-1]-a))
for i in range(N):
    ans = 0
    if i != 0:
        ans = ary[i-1]
        ans += abs(A[i-1]-A[i+1])
    else:
        ans += abs(A[1])
    ans += ary[-1]-ary[i+1]
    print(ans)
