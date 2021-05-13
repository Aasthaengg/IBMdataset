n, a,b= map(int, input().split())
x=list(map(int,input().split()))
y=[int(x[i]-x[i-1]) for i in range(1,n)]
answer=0
for i in y:
  if a*i<=b:
    answer+=a*i
  else:
    answer+=b
print(answer)