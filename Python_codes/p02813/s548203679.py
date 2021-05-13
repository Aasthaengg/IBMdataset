def func(x, y):
  if len(y)==1:
    dic.append(x*10+int(y))
  else:
    for j in range(len(y)):
      func(x*10+int(y[j]), y[:j]+y[j+1:])
dic = []
 
N = int(input())
func(0, "".join([str(i) for i in range(1,N+1)]))
 
A = int(input().replace(" ", ""))
B = int(input().replace(" ", ""))
ans = abs(dic.index(A)-dic.index(B))
print(ans)