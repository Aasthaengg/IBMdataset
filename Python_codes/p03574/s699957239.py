h,w = map(int, input().split())
s = [list(input()) for _ in range(h)]
p = [-1,0,1]
for i in range(h):
  for j in range(w):
    count = 0
    for ph in p:
      for pw in p:
        if (ph==0 and pw==0) or not(0<=i-ph<=h-1) or not(0<=j-pw<=w-1):
          continue
        if s[max(i-ph,0)][max(j-pw,0)]=='#':
          count += 1
    if s[i][j]=='.': s[i][j]=str(count)
for si in s:
  print(''.join(si))