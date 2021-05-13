A, B, C = map(int, input().split())
cnt = B
 
if C <= A + B:
  cnt += C
else:
  cnt += A+B+1
  
print(cnt)