def main():
  A = input()
  N = len(A)
  ans = 0
  for i in range(26):
    c = ord('a')+i
    c = chr(c)
    m = A.count(c)
    ans += m*(m-1)//2
  print(N*(N-1)//2-ans+1)
if __name__=='__main__':
  main()