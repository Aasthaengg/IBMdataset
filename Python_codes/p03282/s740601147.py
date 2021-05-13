S = input()
K = int(input())
for i in range(min(len(S), K)):
  if(S[i] != '1' and S[i] != '0'):
    print(int(S[i]))
    exit()
print(1)