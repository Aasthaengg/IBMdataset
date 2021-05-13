
def main():
  S = input()
  middle = int(len(S) / 2)
  ans = 0
  
  for i in range(0, middle):
    if S[i] != S[-(i+1)]:
      ans += 1
  
  print(ans)
      
  
  
  
main()