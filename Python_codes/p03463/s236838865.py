def main():
  t = input().split(" ")
  N, A, B = int(t[0]), int(t[1]), int(t[2])
  
  if (B-A) % 2 == 0:
    print("Alice")
  else:
    print("Borys")
main()