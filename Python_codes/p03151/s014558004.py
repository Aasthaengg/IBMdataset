N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

if sum(A) < sum(B) :
    print(-1)
    exit()

les = 0
ans = 0
Over = []
for i in range(N) :
    Over.append(A[i]-B[i])
    if A[i] < B[i] :
        les += B[i] - A[i]
        ans += 1

Over.sort(reverse = True)
for ov in Over :
    if les <= 0 :
        print(ans)
        break
    les -= ov
    ans += 1
