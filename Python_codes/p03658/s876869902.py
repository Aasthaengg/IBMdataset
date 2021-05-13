def main():
  n,k = list(map(int,input().split()))
  l = list(map(int,input().split()))
  l.sort(reverse=True)
  sum=l[0]
  for i in range(1,k):
    sum+=l[i]
  print(sum)
    
main()