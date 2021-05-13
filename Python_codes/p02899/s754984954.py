n = int(input())
a = list(map(int,input().split()))
ans = [0]*n
for index,aa in enumerate(a):
  ans[aa-1] = index+1
print(*ans)