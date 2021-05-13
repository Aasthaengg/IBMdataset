def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    N = Z()
    A, B, C = [], [], []
    for i in range(N):
        a, b = ZZ()
        A.append(a)
        B.append(b)
        C.append([a+b, i])
    C.sort(reverse=True)
    output = 0
    for i in range(N):
        _, j = C[i]
        if i%2 == 0: output += A[j]
        else: output -= B[j]
    print(output)

    return

if __name__ == '__main__':
    main()
