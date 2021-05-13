def main():
  x = int(input())
  x, y = divmod(x, 11)
  ret = 2 * x + (y+5) // 6
  print(ret)

if __name__ == '__main__':
  main()