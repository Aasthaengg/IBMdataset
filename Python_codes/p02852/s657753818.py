import sys
#input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n,m = map(int,input().split())
s = list(input())
s.reverse()
list1 = []
def maze(mass,times): #今いるマス、現状の手数
  if mass+m >= n:
    list1.append(str(n-mass))
    return
  for i in range(m,0,-1):
    if s[mass+i] == "0":
      list1.append(str(i))
      maze(mass+i,times+1)
      return
    elif i == 1:
      print("-1")
      exit()
  return

a = maze(0,0)
list1.reverse()
print(" ".join(list1))