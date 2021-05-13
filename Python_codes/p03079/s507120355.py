print_val = "No"
 
A, B, C = map(int, raw_input().split())

if A == B and B == C:
  print_val = "Yes"

print print_val