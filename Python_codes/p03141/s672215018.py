from sys import stdin
n = int(stdin.readline().rstrip())
AB = [list(map(int,stdin.readline().rstrip().split())) for _ in range(n)]
kouhuku = [i[0]+i[1] for i in AB]
kouhuku.sort(reverse=True)
aoki = sum(i[1] for i in AB)
takahashi = sum(kouhuku[::2])
print(takahashi-aoki)