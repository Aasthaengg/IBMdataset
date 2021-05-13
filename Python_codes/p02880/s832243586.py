n = int(input())

def solve(n: int) -> str:
  for l in range(1, 10):
    for m in range(1, 10):
      if n == l * m:
        return "Yes"
  return "No"
  
print(solve(n))