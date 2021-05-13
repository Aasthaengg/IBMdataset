n = int(input())

tmp = [0]
a = []
b = []
ans = 0
for i in range(n):
  tmp[0] = list(map(int,input().split()))
  a.append(tmp[0][0])
  b.append(tmp[0][1])
  
ans = max(a)
#print(ans)
print(ans+min(b))
