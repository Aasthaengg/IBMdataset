from functools import partial

N = int(input())
S = input()
lst = [chr(ord("A")+i) for i in range(26)]

def convert(x,n,l):
  id = ord(x) - ord("A")
  return l[(id+n)%26]

ans = "".join(map(partial(convert,n=N,l=lst),S))
print(ans)