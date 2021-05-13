a, b, c = input().split()
ans = "No"
if (a == b and a != c) or (a == c and a != b) or (b == c and a != b):
  ans  = "Yes"
print(ans)