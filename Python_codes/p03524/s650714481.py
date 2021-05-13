def main():
  S = input()
  x = S.count("a")
  y = S.count("b")
  z = S.count("c")
  if max(abs(x - y), abs(y - z), abs(z - x)) <= 1:
    print("YES")
  else:
    print("NO")

if __name__ == "__main__":
  main()