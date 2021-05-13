S = list(input())
count = 0
for i in range(3):
  if S[i] == S[i+1]:
    count += 1
print("Bad" if count > 0 else "Good")