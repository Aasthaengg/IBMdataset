import re

S=input()

if re.fullmatch('([a-z]*)keyence',S):
  print('YES')
elif re.fullmatch('k([a-z]*)eyence',S):
  print('YES')
elif re.fullmatch('ke([a-z]*)yence',S):
  print('YES')
elif re.fullmatch('key([a-z]*)ence',S):
  print('YES')
elif re.fullmatch('keye([a-z]*)nce',S):
  print('YES')
elif re.fullmatch('keyen([a-z]*)ce',S):
  print('YES')
elif re.fullmatch('keyenc([a-z]*)e',S):
  print('YES')
elif re.fullmatch('keyence([a-z]*)',S):
  print('YES')
else:
  print('NO')