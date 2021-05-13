n = int(input())
S = list(map(int,input().split()))
q = int(input())
T = list(map(int,input().split()))

S = list(set(S))

cnt = 0
for i in S:
    if i in T:
        cnt+=1
print(cnt)
