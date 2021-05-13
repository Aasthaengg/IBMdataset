A,B,M=map(int,input().split())
l_a=list(map(int,input().split()))
l_b=list(map(int,input().split()))
ans=[min(l_a)+min(l_b)]
for i in range(M):
  xi,yi,ci=map(int,input().split())
  ans.append(l_a[xi-1]+l_b[yi-1]-ci)
print(min(ans))