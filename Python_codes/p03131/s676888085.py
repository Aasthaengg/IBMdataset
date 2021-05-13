K, A, B = map(int, input().split())

ans = 1
yen = 0
if A+1 >= B:
    print(K+1)
    quit()
cycle = max(0, (K-(A-1))//2)
res = (K-(A-1)) % 2
ans = cycle * (B-A) + A + res
print(ans)