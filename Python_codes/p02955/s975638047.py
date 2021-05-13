N, K = map(int, input().split())
A = list(map(int, input().split()))

sumA = sum(A)
candiate = []
# sumAの約数を列挙する
tmp = 1
while tmp * tmp <= sumA:
    if sumA % tmp == 0:
        candiate.append(tmp)
        candiate.append(sumA // tmp)
    tmp += 1

def f(x):
    A.sort(key=lambda z:z%x)
    tmp = 0
    judge = True
    for a in A:
        if tmp + (a % x) <= K and judge:
            tmp += a % x
        else:
            judge = False
            tmp -= x - (a % x)
        if tmp < 0: return False
    return True
ans = -1
for cand in candiate:
    if f(cand):
        ans = max(ans, cand)

print(ans)
