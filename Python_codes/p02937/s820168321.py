from bisect import bisect_right
def main():
  s=input()
  t=input()
  n=len(t)
  m=len(s)
  lindex=[[] for _ in range(26)]
  for i in range(m):
    if s[i] in t:
      lindex[ord(s[i])-97].append(i)
  for i in range(n):
    if len(lindex[ord(t[i])-97])==0:
      print(-1)
      exit()
  cnt=0
  inde=-1
  for i in range(n):
    l=len(lindex[ord(t[i])-97])
    idx=bisect_right(lindex[ord(t[i])-97],inde)
    if l==idx:
      cnt+=1
      inde=lindex[ord(t[i])-97][0]
    else:
      inde=lindex[ord(t[i])-97][idx]
  return print(m*cnt+inde+1)
if __name__=='__main__':
  main()