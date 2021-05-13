N = int(input())
A = list(map(int, input().split()))

def TwoNumber(a):
    ans = 0
    while True:
        if a % 2==0:
            a = a /2
            ans += 1
        else:
            break
    return ans

ans = 0
for i in range(len(A)):
    ans += TwoNumber(A[i])

print(ans)