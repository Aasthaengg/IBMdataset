S = input()
T = input()
 
def match_num_character(x, y):
  count = 0
  for a, b in zip(x, y):
    if a == b:
      count += 1
      
  return count
 
length = len(T)
max_count = max([match_num_character(S[i:i+length], T) for i in range(1+len(S) - length)])
 
print(length - max_count)