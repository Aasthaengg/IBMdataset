A,B=map(int,input().split())
num = 1
ans = 0
while num < B:
    num += A - 1
    ans += 1
print(ans)