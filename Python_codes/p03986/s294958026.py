def main():
  S = str(input())
  ans = 0
  num_t = 0
  for i in range(len(S)-1, -1, -1):
    if S[i] == 'T':
      flag = True
      num_t += 1
    if S[i] == 'S' and num_t > 0 :
      num_t -= 1
      ans += 2
  print(len(S)-ans)
  
if __name__ == "__main__":
  main()