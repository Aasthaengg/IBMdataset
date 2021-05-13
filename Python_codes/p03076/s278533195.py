import copy
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

m = [a, b, c, d, e]

ans = 10 ** 10
def order(t, mr):
  global ans
  if len(mr) == 0:
    ans = min(ans, t)
    return
  
  if t % 10 != 0:
    t = t - (t % 10) + 10
  for i in range(len(mr)):
    nextt =  t + mr[i]
    nextmr = copy.deepcopy(mr)
    del nextmr[i]
    order(nextt, nextmr)
order(0, m)
print(ans)