n = int(input())
A = list(map(int,input().split()))

ans = 0
for a in A:
    tmp = 0
    while a%2 == 0:
        tmp += 1
        a = a//2
    ans += tmp

print (ans)
