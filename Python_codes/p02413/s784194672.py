r,c = [eval(x) for x in input().split()]
table = [[eval(x) for x in input().split()] for _ in range(r)]
[table[i].append(sum(table[i])) for i in range(r)]
table.append([sum([table[i][j] for i in range(r)]) for j in range(c+1)])
[print(''.join([str(table[i][j]) + (' ' if j != c else '') for j in range(c+1)])) for i in range(r+1)]