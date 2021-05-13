N = int(input())
arr = list(map(str, input().strip().split()))

if len(set(arr)) == 4:
  print("Four")
elif len(set(arr)) == 3:
  print("Three")