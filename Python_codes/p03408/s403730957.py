n=int(input())
s=[]
t=[0]*101
for _ in range(n):
    si=input()
    if si not in s:s.append(si)
    t[s.index(si)]+=1
m=int(input())
for _ in range(m):
    si=input()
    if si in s:t[s.index(si)]-=1
print(max(0,max(t)))


