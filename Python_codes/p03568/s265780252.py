N = int(input())
A = list(map(int,input().split()))
N**3
cnt = 0
for i in A:
    if i%2 == 0:
        cnt += 1
ans = 3**N - 2**cnt
print(ans)