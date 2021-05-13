def main():
    A, B, C = map(int, input().split())
    K = int(input())
    for i in range(K):
        if A >= B and A >= C:
            A = 2*A
        if B >= A and B >= C:
            B = 2*B
        if C >= A and C >= B:
            C = 2*C
    print(sum([A, B, C]))
main()