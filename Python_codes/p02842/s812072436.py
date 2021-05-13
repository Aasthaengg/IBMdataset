X = int(input())
ans = int(X/1.08)
if int(ans*1.08) == X:
  print(ans)
elif int((ans+1)*1.08) == X:
  print(ans+1)
else:
  print(':(')