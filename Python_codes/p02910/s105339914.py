S = input()
for i in range(len(S)+1):
  if i == len(S):
    print('Yes')
    break
  if S[i] =='U' or S[i] =='D':
    pass
  else:
    if i % 2 ==0:
      if S[i] == 'R':
        pass
      else:
        print('No')
        break
    else:
      if S[i]== 'L':
        pass
      else:
        print('No')
        break
        
      
    
