n = int(input())
a = input()
b = input()
c = input()

cnt = 0
for i in range(n):
    tmp_lists = [a[i], b[i], c[i]]
    sets = set(tmp_lists)
    cnt += len(sets) - 1

print(cnt)