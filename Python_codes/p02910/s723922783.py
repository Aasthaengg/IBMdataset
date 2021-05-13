S=input()
for i,s in enumerate(S):
  if ((i+1)%2 == 1 and s=='L') or ((i+1)%2==0 and s=='R'):
    print('No')
    exit()
print('Yes')
