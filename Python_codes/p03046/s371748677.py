m, k = map(int, input().split())

if k > 2 ** m - 1 or m == 1 and k == 1:
    print(-1)
    quit()

if k == 0:
    print(' '.join(map(lambda x : str(x // 2), range(0, 2 ** (m + 1)))))
    quit()

a = list(range(0, 2 ** m)) 
a.remove(k)
ans = a + [k]
a.reverse()
ans += a + [k]
print(' '.join(map(str, ans)))