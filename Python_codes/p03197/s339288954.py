def main():
  n=int(input())
  for _ in range(n):
    a=int(input())
    if a&1:
      return "first"
  return "second"

ans=main()
print(ans)