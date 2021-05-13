N, M = map(int, input().split())
A = [input() for _ in range(N)]
B = [input() for _ in range(M)]

if N == M:
    if A == B:
        print("Yes")
    else:
        print("No")
    exit()

for a_i in range(N-M):
    if B[0] in A[a_i]:
        #スタート地点を記憶
        start = []
        for a_j in range(N-M+1):
            if B[0] == A[a_i][a_j:M+a_j]:
                start.append(a_j)
        for s in start:
            f = True
            for b_i in range(M):
                #記録したスタート地点の列で、他の行も一致するか確認
                if B[b_i] != A[a_i+b_i][s:s+M]:
                    f = False
            if f == True:
                print("Yes")
                exit()
print("No")