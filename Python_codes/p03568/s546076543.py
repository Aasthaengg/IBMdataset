n = int(input())
A = list(map(int,input().split()))

ans = 3**n
aa = 1
for i in A:
    if i%2==0:aa*=2

print(ans-aa)