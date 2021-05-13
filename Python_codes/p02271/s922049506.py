num_n = int(input())
n = [int(x) for x in input().split()]
num_m = int(input())
m = [int(x) for x in input().split()]
     
def solve(i, m):
   if m == 0:
      return True
   if i >= num_n or m > sum(n):
      return False
   res = solve(i + 1, m) or solve(i + 1,m - n[i])
   return res
      
for k in range(num_m):
   if solve(0, m[k]):
      print ("yes")
   else:
      print ("no")
