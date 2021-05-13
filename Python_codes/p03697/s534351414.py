def main():
  a,b = map(int,input().split())
  ans = a + b
  print("error" if ans >= 10 else ans)
if __name__ == '__main__':
  main()