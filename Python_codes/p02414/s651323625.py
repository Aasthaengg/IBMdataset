n,m,l = [int(x) for x in input().split( )]
zeros1 = [[0 for x in range(m)] for y in range(n)]
zeros2 = [[0 for x in range(l)] for y in range(m)]
for i in range(n):
    retsu = [int(x) for x in input().split( )]
    zeros1[i] = retsu
for j in range(m):
    retsu2 = [int(x) for x in input().split( )]
    zeros2[j] = retsu2
answer = []
for i in range(n):
    mini_answer = []
    for j in range(l):
        value = 0
        for k in range(m):
            value += zeros1[i][k]*zeros2[k][j]
        mini_answer.append(value)
    answer.append(mini_answer)
for x in answer:
    print(*x)


