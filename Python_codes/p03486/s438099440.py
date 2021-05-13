s=input()
t=input()

temps=sorted(s)
tempt=sorted(t)
sp=''.join(temps)
tp=''.join(tempt)
tp=tp[::-1]
if sp<tp:
  print('Yes')
else:
  print('No')