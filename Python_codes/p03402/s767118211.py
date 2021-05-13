A, B = map(int, input().split())
a,p = divmod(A-1,50)
b,q = divmod(B-1,50)
ans = []
cnt = 0
for i in range(2*a):
  if i%2==0:
    ans += ['.#'*50]
  else:
    ans += ['#'*100]
cnt += 2*a

if p!=0:
  ans += ['.#'*p+'#'*(100-2*p)]
  cnt += 1
ans += ['#'*100]
ans += ['.'*100]
cnt += 2
for i in range(2*b):
  if i%2==0:
    ans += ['.#'*50]
  else:
    ans += ['.'*100]
cnt += 2*b
if q!=0:
  ans += ['.#'*q+'.'*(100-2*q)]
  cnt += 1
print(cnt,100)
print('\n'.join(ans))