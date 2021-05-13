n = int(input())
slst = []
tlst = []
for _ in range(n):
  s,t = map(str,input().split())
  slst.append(s)
  tlst.append(int(t))
x = input()
print(sum(tlst[slst.index(x)+1:]))