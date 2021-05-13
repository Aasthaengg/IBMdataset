N,M = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)
A_list = A[:M]

vote_sum = sum(A)
ans = 0

for i in A_list:
    if i/vote_sum < 1/(4*M):
        print("No")
        break
    else:
        ans +=1
if ans == M:
    print("Yes")