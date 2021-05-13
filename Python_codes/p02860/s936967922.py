def main():
  n=int(input())
  s=input()
  if s[:int(len(s)/2)]==s[int(len(s)/2):]:
    print("Yes")
  else:
    print("No")
main()