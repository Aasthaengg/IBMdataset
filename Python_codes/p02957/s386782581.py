A, B= map(int, input().split())
diff_ba = B-A
if diff_ba % 2 == 0:
  print(A + diff_ba//2)
else:
  print("IMPOSSIBLE")