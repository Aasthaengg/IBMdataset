N = int(input())
A = [0] + list(map(int, input().split()))

num = {}


# def xC2
def calc(x):
    return x*(x-1)//2


for a in A[1:]:
    if a not in num:
        num[a] = 0
    num[a] += 1

pattern = 0

for n in num:
    pattern += calc(num[n])

for i in range(1, N+1):
    n = num[A[i]]
    ans = pattern - calc(n) + calc(n-1)
    print(ans)

