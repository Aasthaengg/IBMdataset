A, B, C = map(int,input().split())
cnt = 0
if C >= A:
  m = C-A
  cnt += A
  if m > B:
    cnt += B*2+1
  elif m==B:
    cnt += B*2
  else:
    cnt += m+B
else:
  cnt += B+C
print(cnt)