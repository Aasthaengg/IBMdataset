S=input()

ans='Yes'
for i in range(len(S)):
  if (i%2==1) and (S[i] not in {'L','U','D'}):ans='No'
  if (i%2==0) and (S[i] not in {'R','U','D'}):ans='No'
print(ans)