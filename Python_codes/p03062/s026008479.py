N = int(input())
A = list(map(int,input().split()))

mns = len([i for i in A if i < 0])

if mns % 2 == 0:
  ans = sum([abs(i) for i in A])
else:
  ans = sum([abs(i) for i in A]) - 2 * min([abs(i) for i in A])
  
print(ans)