H,W=map(int,input().split())
result = []
for i in range(H+2):
  if i == 0 or i == H+1:
    result.append(''.join(['#' for _ in range(W+2)])) 
  else:
    word = input()
    result.append('#'+word+'#')
[print(i) for i in result]