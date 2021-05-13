n=int(input())
A,B=map(int, input().split())
P=list(map(int, input().split()))
s=[]
w=[]
t=[]
l=[s,w,t]
for i in range(n):
  if P[i]<=A:
    s.append(P[i])
  elif P[i]>=A+1 and P[i]<=B:
    w.append(P[i])
  else:
    t.append(P[i])
print(min(len(s),len(w),len(t)))

