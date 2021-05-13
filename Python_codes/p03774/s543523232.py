def main():
  n,m = list(map(int,input().split()))
  ab = [map(int, input().split()) for _ in range(n)]
  a, b = [list(i) for i in zip(*ab)]
  cd = [map(int, input().split()) for _ in range(m)]
  c, d = [list(i) for i in zip(*cd)]
  
  for i in range(0,n):
    min=abs(a[i]-c[0])+abs(b[i]-d[0])
    min_index=0
    for j in range(1,m):
      if min>abs(a[i]-c[j])+abs(b[i]-d[j]):
        min=abs(a[i]-c[j])+abs(b[i]-d[j])
        min_index=j
    print(min_index+1)
  
main()