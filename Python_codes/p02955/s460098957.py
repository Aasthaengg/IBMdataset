N, K = map(int, input().split())
A = list(map(int, input().split()))


def divisors(n: int) -> dict:
    divs = []
    for i in range(1, (int(n**0.5)+1)):
        if n % i == 0:
            divs.append(i)
            if i != n//i:
                divs.append(n//i)
    return divs


def solve(B, f):
    cost = sum(B)
    cost = sum(B[:-cost//f])
    return cost


fct = divisors(sum(A))
for f in sorted(fct, reverse=True):
    B = sorted([b % f for b in A])
    cost = solve(B, f)
    if K >= cost:
        print(f)
        quit()