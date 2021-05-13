n=input()
for i in range(n):
  inl=map(int, raw_input().split())
  inl.sort()
  if inl[0]**2+inl[1]**2==inl[2]**2:
    print "YES"
  else:
    print "NO"