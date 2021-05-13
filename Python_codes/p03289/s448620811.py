S = str(input())
    
result = False
    
    
if S[0] == 'A':
    
    check = S[2:len(S)-1]
    
    if check.count('C') == 1:
        index = check.find('C') + 2
        
        if S[1:index].islower() and S[index+1:].islower():
            result = True
            
if result:
    print('AC')
else:
    print('WA')