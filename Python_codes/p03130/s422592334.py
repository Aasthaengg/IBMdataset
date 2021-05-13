ans_list = [0]*4

for i in range(3):
  a, b = [ int(v)-1 for v in input().split() ]
  ans_list[a] += 1
  ans_list[b] += 1

print( "YES" if sorted(ans_list) == [1,1,2,2] else "NO" )