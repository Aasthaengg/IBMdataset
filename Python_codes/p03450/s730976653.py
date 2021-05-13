n, m = map(int, input().split())
D = [list(map(int, input().split())) for i in range(m)]

A = [0] * (n+1)

M = [[] for i in range(n+1)]

for i in range(m):
    M[D[i][0]].append([D[i][1], D[i][2]])
    M[D[i][1]].append([D[i][0], -D[i][2]])

V = [0] * (n+1)


# print(M)

for ii in range(1, n+1):
    if V[ii] == 0 and len(M[ii]) > 0:

        Q = [[ii, 0]]
        st = 0
        while st < len(Q):
            # print(A,V,Q)
            node = Q[st][0]
            dist = Q[st][1]
            if V[node] == 0 and len(M[node]) > 0:
                V[node] = 1
                A[node] += dist
                for i in M[node]:
                    if V[i[0]] == 0:
                        Q.append([i[0], A[node] + i[1]])
            st += 1

# print(A)

def d():
    for i in range(m):
        if A[D[i][1]] - A[D[i][0]] != D[i][2]:
            return "No"
    return "Yes"

print(d())