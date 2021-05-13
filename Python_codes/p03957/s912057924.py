S = input()
a= S.find('C')
b= S.find('F',a+1)
print('Yes') if a>=0 and b>=0 and a<b else print('No')