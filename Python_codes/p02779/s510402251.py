n = int(input())
ans = set()
puzzle = list(map(int,input().split()))
for x in puzzle:
    ans.add(x)
l = len(ans)
p = len(puzzle)
if l==p:
    print("YES")
else:
    print("NO")