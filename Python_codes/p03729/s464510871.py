def main():
  s1,s2,s3 = map(str,input().split())
  ans = False
  if s1[len(s1)-1] == s2[0]:
    if s2[len(s2)-1]==s3[0]:
      ans = True
  print("YES" if ans else "NO")
if __name__ == '__main__':
  main()