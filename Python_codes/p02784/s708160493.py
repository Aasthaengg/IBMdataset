v, n = map(int, input().split())
arr = sorted(map(int, input().split()))
print("Yes") if sum(arr[-n:]) >= v else print("No")
  
