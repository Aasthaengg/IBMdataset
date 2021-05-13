def abc171_e():
    n = int(input())
    A = list(map(int, input().split()))
    cum = 0
    for a in A:
        cum ^= a
    B = [0] * n
    for i, a in enumerate(A):
        B[i] = cum ^ a
    print(*B, sep=' ')

if __name__ == '__main__':
    abc171_e()