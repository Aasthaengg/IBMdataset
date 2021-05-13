n=int(input())
ab=[]
for _ in range(n):
  ab.append(list(map(int, input().split())))
absort=sorted(ab, key=lambda x:(x[1]))
now=0
for i in range(n):
  now+=absort[i][0]
  if now>absort[i][1]:
    print("No")
    exit()
print("Yes")