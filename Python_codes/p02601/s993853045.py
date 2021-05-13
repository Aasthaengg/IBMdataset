A,B,C = map(int,input().split())
N = int(input())
stack = [(A,B,C,N)]
flag = False
while stack:
  a,b,c,n = stack.pop()
  if a<b and b<c:
    flag = True
    break
  if n>0:
    stack.append((a*2,b,c,n-1))
    stack.append((a,b*2,c,n-1))
    stack.append((a,b,c*2,n-1))
print('Yes') if flag else print('No')

