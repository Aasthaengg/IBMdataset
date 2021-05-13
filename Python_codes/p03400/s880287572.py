N = int(input())
D,X = list(map(int, input().split()))
A = [int(input()) for i in range(N)]
c=[]
for i in A:
    c.append(len(range(1,D+1,i)))
ans = sum(c)+X
print(ans)