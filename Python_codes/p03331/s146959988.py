N = int(input())
if N == 10 or N == 100 or N == 1000 or N == 10000 or N == 100000:
    print(10)
else:
    ans = sum(list(map(int, str(N))))
    print(ans)