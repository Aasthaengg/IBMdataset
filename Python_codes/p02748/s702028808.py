a,b,m = map(int,input().split())
al = list(map(int,input().split()))
bl = list(map(int,input().split()))
yasuiyo = min(al) + min(bl)
ans = []
for i in range(m):
  x,y,c = map(int,input().split())
  ans.append(al[x-1] + bl[y-1] - c)

print(min(min(ans),yasuiyo))