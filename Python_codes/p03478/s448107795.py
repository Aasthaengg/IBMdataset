def sum(n):
    str_n = str(n)
    ans = 0
    for i in range(len(str_n)):
        ans += int(str_n[i])
    return ans

N,A,B = map(int,input().split())

ans1 = 0
for i in range(N+1):
    if A <= sum(i) <= B:
        ans1 += i
    else:
        continue
print(ans1)
