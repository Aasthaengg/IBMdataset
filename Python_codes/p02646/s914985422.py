def main():
  A,V = map(int, input().split())
  B,W = map(int, input().split())
  T = int(input())


  if A<=B:
      after_A=A+V*T
      after_B=B+W*T
      if after_B<=after_A:
          print("YES")
      else:
          print("NO")
  else:
      after_A=A-V*T
      after_B=B-W*T
      if after_A<=after_B:
          print("YES")
      else:
          print("NO")

if __name__=='__main__':
  main()
