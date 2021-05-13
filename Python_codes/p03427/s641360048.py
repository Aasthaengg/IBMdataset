n = input()
ans = 0
for i in range(len(n)):
    tmp = [9]*len(n)
    for j in range(9, -1, -1):
        tmp[i] = j
        s = int(''.join(map(str, tmp)))
        if s <= int(n):
            ans = max(ans, sum(map(int, str(s))))
            break
print(ans)