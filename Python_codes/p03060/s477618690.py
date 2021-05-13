def q2():
    N = int(input())
    V = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]

    ans = 0
    for i in range(N):
        if V[i] - C[i] > 0:
            ans += V[i] - C[i]
    return ans

if __name__ == '__main__':
    print(q2())
