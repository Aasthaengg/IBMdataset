from sys import stdin
 
s = sum([int(x) for x in stdin.readline().rstrip().split()])
 
ans = "win"
if s > 21: ans = "bust"
print(ans)