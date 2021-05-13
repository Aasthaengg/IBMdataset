N=int(input())
s=[]
for i in range(N):
  a=input()
  s.append(a)
b=len(list(set(s)))
print(b)