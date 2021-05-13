n = int(input())
l = [list(map(int,input().split())) for i in range(n)]
ab = []
ans = 0
for i,j in l:
    ab.append(i+j)
    ans -= j

ab.sort(reverse=True)
ans += sum(ab[::2])
print(ans)



