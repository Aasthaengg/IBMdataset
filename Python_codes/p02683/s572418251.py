N, M, X = map(int, input().split())
C = [0] * N
A = [[0] * M] * N

for i in range(N):
    S = list(map(int, input().split()))
    C[i] = S[0]
    A[i] = S[1:]

smallest = None
for i in range(2 ** N):
    sum = 0
    string = ""
    Algo = [0] * M
    for j in range(N):
        if (i >> j) & 1:
            sum += C[j]
            for m in range(M):
                Algo[m] += A[j][m]
            string += "1"
        else:
            string += "0"
    # print(Algo)
    # print(string)
    # print(sum)
    if all(e >= X for e in Algo):
        if smallest == None:
            smallest = sum
        elif sum < smallest:
            # print("更新！")
            smallest = sum

if smallest == None:
    print(-1)
else:
    print(smallest)
