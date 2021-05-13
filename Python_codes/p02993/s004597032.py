S = list(input())
for i in range(0,3,1):
  if S[i]==S[i+1]:
    print("Bad")
    exit()
print("Good")