n = int(input())
arr = list(map(int, input().split()))
term = 0
for i in arr:
  term += 1/i
  
print(1/term)