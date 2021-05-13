N=int(input())
B=list(map(int,input().split(' ')))
ans = []
for i in range(N):
    for n,j in enumerate(B[::-1]):
        if N-i-n==j:
            ans.append(B.pop(N-i-n-1))
            break
if len(ans)==N:
    for i in ans[::-1]:
        print(i)
else:
    print(-1)