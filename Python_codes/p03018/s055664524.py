def main():
  S = str(input())
  s = []
  i = 0
  while i <= len(S)-1:
    if i == len(S)-1:
      s.append(S[i])
      break
    if S[i] == "B" and S[i+1] == "C":
      s.append("D")
      i += 2
    else:
      s.append(S[i])
      i += 1
  ans = 0
  flag = True
  for i in range(len(s)-1, -1, -1):
    if flag and s[i] == "D":
      posi = i
      flag = False
    if not flag and s[i]=="A":
      ans += posi-i
      posi-= 1
    if s[i] == "B" or s[i] == "C":
      flag = True
  print(ans)
  
  
if __name__ == "__main__":
  main()