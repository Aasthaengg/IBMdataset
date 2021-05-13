import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

def main():
    N = int(readline())
    A = [int(i) for i in readline().split()]

    ans = []
    B = [0] * N
    for i in reversed(range(N)):
        s = sum(B[i::i+1])
        if s % 2 == A[i]:
            continue
        else:
            B[i] += 1
            ans.append(i+1)
    
    print(sum(B))

    if len(ans):
        print(*ans)


if __name__ == "__main__":
    main()
