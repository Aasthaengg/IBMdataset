def main():
  n,m = list(map(int,input().split()))
  dic={}
  for i in range(1,n+1):
    dic[i]=0
  for _ in range(m):
    b, c = map(int, input().split())
    dic[b]+=1
    dic[c]+=1
  for i in range(1,n+1):
    print(dic[i])

main()