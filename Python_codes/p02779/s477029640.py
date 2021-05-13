n = int(input())
al = list(map(int, input().split()))

a_s = set()
for a in al:
    if a in a_s:
        print('NO')
        break
    a_s.add(a)
else:
    print('YES')