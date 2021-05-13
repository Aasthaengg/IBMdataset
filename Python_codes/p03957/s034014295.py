def check():
  S = input()
  ind = S.find('C')
  if ind==-1:
    return 'No'
  ind2 = S[ind+1:].find('F')
  if ind2==-1:
    return 'No'
  return 'Yes'
print(check())