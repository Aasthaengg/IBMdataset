def check():
  S = input()
  T = input()
  S *= 2
  for i in range(len(T)):
    if S[i:i+len(T)]==T:
      return 'Yes'
  return 'No'
print(check())