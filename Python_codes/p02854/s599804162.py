n = int(input())
a = list(map(int, input().split()))

mid = sum(a)/2
cum = 0
diff = 10**10
for each in a:
  cum += each
  diff = min(diff, abs(mid-cum))
  
print(int(diff/0.5))