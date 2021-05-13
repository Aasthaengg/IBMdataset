n = int(input())
ls = sorted(list(map(int,input().split())))

ans = 0
for i in range(len(ls)-2) :
  a = ls[i]
  for j in range(len(ls)-i-2) :
    b = ls[i+1+j]
    for k in range(len(ls)-i-j-1) :
      c = ls[i+j+k+1]
      if b-a < c < b+a and a!=b!=c!=a :
        ans += 1
print(ans)