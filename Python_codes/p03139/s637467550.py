#岩田くんのアドバイスからmapを使って作り直したもの

rec = input().split()
n, a, b = map(int, rec)
nin = [a, b]

nmax = min(nin)
nmin = n - min(n, (n - nin[0]) + (n - nin[1]))
print(str(nmax) + " " + str(nmin))