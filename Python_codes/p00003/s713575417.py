N = int(input())
ary=[]
ans=[]
for i in range(N):
    ary.append(list(map(int,(input().split()))))
    if 2 * max(ary[-1]) ** 2 == sum(ary[-1][j] ** 2 for j in range(3)):
        ans.append('YES')
    else:
        ans.append('NO')
print('\n'.join(ans))