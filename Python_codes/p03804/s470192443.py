s = input().split()

n = int(s[0])
m = int(s[1])

N = [[0 for j in range(n)] for i in range(n)]

M = [[0 for j in range(m)] for i in range(m)]

for num in range(n):
    p = input()
    words = list(p)
    for number in range(n):
        N[num][number] = words[number]

for num in range(m):
    p = input()
    words = list(p)
    for number in range(m):
        M[num][number] = words[number]



exist = False

for num in range(n):
    for number in range(n):
        if num + m - 1 >= n or number + m - 1 >= n:
            continue

        check = True
        for i in range(m):
            for j in range(m):
                if N[num + i][number + j] != M[i][j]:
                    check = False
        
        if check:
            exist = True

if exist:
    print('Yes')
else:
    print('No')

