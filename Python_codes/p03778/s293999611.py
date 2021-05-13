w,a,b = list(map(int, input().strip().split()))

result = 0
if a+w < b:
  result = b-(a+w)
elif b+w < a:
  result = a-(b+w)

print(result)