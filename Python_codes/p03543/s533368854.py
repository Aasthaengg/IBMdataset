N = str(input())
a, b, c, d = N[0], N[1], N[2], N[3]

ans = "No"
if a == b and b == c:
  ans = "Yes"
elif b == c and c == d:
  ans ="Yes"
    
    
print(ans)
