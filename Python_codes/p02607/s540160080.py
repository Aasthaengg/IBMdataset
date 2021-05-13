N = int(input())
A = [int(i) for i in input().split()]
cnt = 0
for ind, i in enumerate(A):
    cnt += 1 if ((ind+1) * i)%2==1 else 0
print(cnt)