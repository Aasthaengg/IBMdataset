import sys

def input():
    return sys.stdin.readline().strip()

def main():

    N,M = map(int,input().split())
    A = sorted(list(map(int,input().split())))
    BC = [list(map(int,input().split())) for _ in range(M)]
    BC = sorted(BC,reverse=True,key=lambda x: x[1])
    D = []

    for B,C in BC:
        for b in range(B):
            if len(D) != N:
                D.append(C)
            else:
                break
        else:
            continue
        break

    for i in range(len(D)):
        if A[i] < D[i]:
            A[i] = D[i]
        else:
            break

    print(sum(A))

if __name__ == "__main__":
    main()