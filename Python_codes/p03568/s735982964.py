n = int(input())
A = list(map(int,input().split()))
ans = 0
cnt = 0
for a in A:
    if a%2 == 0:
        cnt+=1
print(3**n - 2**cnt)