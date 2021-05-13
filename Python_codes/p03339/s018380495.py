n = int(input())
s = input()

to_east = 0
to_west = s.count('E', 1)
ans = to_east+to_west

for i in range(1, n):
  if s[i-1]=='W':
    to_east += 1
  if s[i]=='E':
    to_west -= 1
  ans = to_east+to_west if ans>to_east+to_west else ans
  
print(ans)

