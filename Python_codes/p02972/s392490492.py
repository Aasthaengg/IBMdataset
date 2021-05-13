def div(n):
    lower_div, upper_div = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_div.append(i)
            if i != n // i:
                upper_div.append(n // i)
        i += 1
    return lower_div + upper_div[::-1]

def main():
    n = int(input())
    A = list(map(int, input().split()))
    L = [0] * n
    b = []
    for i in reversed(range(n)):
        if A[i] != L[i] % 2:
            b.append(i+1)
            d = div(i + 1)
            for j in d:
                L[j-1] += 1
    print(len(b))
    print(*b)

main()
