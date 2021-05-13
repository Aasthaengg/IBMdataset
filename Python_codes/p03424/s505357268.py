N = int(input())
S = list(map(str,input().split()))

S = list(set(S))

if len(S) == 3:
  ans = 'Three'
else:
  ans = 'Four'

print(ans)