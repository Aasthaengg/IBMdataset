n = int(input())
A = list(map(int, input().split()))

A = [i for i in A if i%2==0]
if len(A) != n:
    print(0)
    exit()
cnt = 0
while len(A) == n:
    A = [i//2 for i in A if i%2==0]
    cnt += 1
print(cnt-1)