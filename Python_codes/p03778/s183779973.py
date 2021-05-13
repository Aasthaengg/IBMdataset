def main():
  w,a,b = list(map(int,input().split()))
  if (a+w)<=b or b+w<=a:
    if abs(a+w-b)<=abs(b+w-a):
      print(abs(a+w-b))
    else:
      print(abs(b+w-a))
  else:
    print(0)
main()