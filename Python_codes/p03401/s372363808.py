n = int(input())
l = [0]+list(map(int,input().split()))+[0]
s = 0
for j in range(len(l)-1):
    s += abs(l[j+1]-l[j])
for i in range(1,n+1):
  a = l[i-1]
  b = l[i]
  c = l[i+1]
  if a<=b<=c:
    print(s)
  elif a<=c<=b:
    print(s-2*(b-c))
  elif b<=a<=c:
    print(s-2*(a-b))
  elif b<=c<=a:
    print(s-2*(c-b))
  elif c<=a<=b:
    print(s-2*(b-a))
  elif c<=b<=a:
    print(s)