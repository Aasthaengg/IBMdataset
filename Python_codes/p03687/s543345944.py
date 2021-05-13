s = list(input())
al = [chr(i) for i in range(97, 97+26)]
ans = []

for a in al:
    c = 0
    if s.count(a) == 0:
        continue
    temp = s.copy()
    while not all(i == a for i in temp):
        c += 1
        n_temp = temp.copy()
        for n, j in enumerate(temp):
            if n == 0 and j == a:
                continue
            elif j == a:
                n_temp[n-1] = a
        temp = n_temp[:len(temp)-1]
    ans.append(c)
print(min(ans))