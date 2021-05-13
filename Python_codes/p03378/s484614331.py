def main():
  n,m,x = list(map(int,input().split()))
  a = list(map(int,input().split()))
  
  for i in range(0,m):
    if a[i]>x:
      if i<m-i:
        print(i)
      else:
        print(m-i)
      break
main()
