N = int(input())
A = list(map(int, input().split()))
ans = 0
def yo(n):
    return n%2
def waru(n):
    return int(n / 2)

for i in range(200):
    B = list(map(yo, A))
    if sum(B) == 0:
        A = list(map(waru, A))
        ans += 1
print(ans)