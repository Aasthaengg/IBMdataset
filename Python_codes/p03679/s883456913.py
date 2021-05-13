def main():
  x,a,b = map(int,input().split())
  sumb = (x - a) + b - x
  if x >= sumb:
    ans = "safe"
  if 0 >= sumb:
    ans = "delicious"
  if x < sumb:
    ans = "dangerous"
  print(ans)
if __name__ == '__main__':
  main()