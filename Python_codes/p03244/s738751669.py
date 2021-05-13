from collections import Counter
def main():
    n = int(input())
    A = list(map(int, input().split()))
    A1 = A[::2]
    A2 = A[1::2]
    C1 = Counter(A1).most_common()
    C2 = Counter(A2).most_common()
    if len(set(A)) == 1:
        print(n // 2)
    elif C1[0][0] == C2[0][0]:
        print(n - max(C1[0][1] + C2[1][1], C1[1][1] + C2[0][1]))
    else:
        print(n - C1[0][1] - C2[0][1])

if __name__ == '__main__':
    main()
