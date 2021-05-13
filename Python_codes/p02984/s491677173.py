N = int(input())
A = list(map(lambda x: int(x), input().split()))

a = 0
for i in range(N):
    if i%2 == 0:
        a+=A[i]
    else:
        a-=A[i]

answer = [a]
for i in range(N-1):
    answer.append((A[i]-answer[-1]//2)*2)

print(" ".join(str(i) for i in answer))