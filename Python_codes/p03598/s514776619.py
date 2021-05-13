N = int(input())
K = int(input())
x = list(map(int, input().split()))

ans = 0
for i in x:
    ans += min(abs(i-0), abs(i-K))
print(ans*2)