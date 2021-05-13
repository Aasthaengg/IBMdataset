ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

s = [_ for _ in input()]
ans = [0]*len(s)

last = 'R'


for ri in range(2):
  cnt=0
  for i in range(len(s)):
    if s[i]=='R':
      cnt+=1
    else:
      ans[i]+=cnt//2
      ans[i-1]+=(cnt+1)//2
      cnt=0

  ans=ans[::-1]
  s=s[::-1]
  for i in range(len(s)):
    if s[i]=='L':
      s[i]='R'
    else:
      s[i]='L'


print(' '.join([str(_) for _ in ans]))
