def palindrome(S):
  for i in range(len(S)//2):
#    print(S[i],S[-(i+1)])
    if S[i] != S[-(i+1)]:
      return 0
  return 1
ans = "No"
S = input()
S1 = S[:(len(S)-1)//2]
S2 = S[(len(S)+1)//2:]
#print(palindrome(S))
#print(palindrome(S1))
#print(palindrome(S2))

if palindrome(S) == 1:
  if palindrome(S1) == 1:
    if palindrome(S2) == 1:
      ans = "Yes"
print(ans)