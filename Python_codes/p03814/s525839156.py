def main():
  s=str(input())
  print(s.rfind("Z") - s.find("A") + 1)
if __name__ == "__main__":
    main()