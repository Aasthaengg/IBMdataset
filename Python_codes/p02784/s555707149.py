def main():
  h,n = list(map(int,input().split()))
  a = list(map(int,input().split()))
  if sum(a)>=h:
    print("Yes")
  else:
    print("No")
main()