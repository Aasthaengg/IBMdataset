n = int(input())
A = list(map(int, input().split()))
B = [a - i for i, a in enumerate(A)]
B.sort()
def median(list):
    L = sorted(list)
    n = len(L)
    m = int(n/2)
    if n % 2 == 0:
        return (L[m - 1] + L[m]) / 2
    else:
        return L[(n - 1) // 2]
b = int(median(B))
print(sum(abs(x - b) for x in B))