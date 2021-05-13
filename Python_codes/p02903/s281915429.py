H,W,A,B = map(int,input().split())

ans = []
for i in range(B):
  row = '1'*A+'0'*(W-A)
  ans.append(row)

for i in range(H-B):
  row = '0'*A+'1'*(W-A)
  ans.append(row)

print(*ans,sep='\n')