N = int(input())
S1 = input()
S2 = input()
count = 1

if(S1[0] == S2[0]):
  ans= 3
else:
  ans= 6
  count+= 1

while count < N:
  if(S1[count] == S2[count]):
    if(S1[count- 1] == S2[count- 1]):
      ans*= 2
      count+= 1
    else:
      count+= 1
  else:
    if(S1[count- 1] == S2[count- 1]):
      ans*= 2
      count+= 2
    else:
      ans*= 3
      count+= 2
      
print(ans% (10** 9+ 7))