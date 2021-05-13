n =int(input())
s=[""]*n
t=[0]*n
for i in range(n):
    s[i],t[i] = input().split()
    t[i] = int(t[i])
r = [0] * (n+1)
for i in range(1,n+1):
  r[i] = r[i-1] + t[i-1]
x=input()
ind = s.index(x)
print(r[n] - r[ind+1])