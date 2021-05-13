import sys
S = input()
for i in range(1,len(S)):
  if S[i] == S[i-1]:
    print("Bad")
    sys.exit()
print("Good")