S = input()
i1 = S.find('C')
i2 = S.rfind('F') 
print('Yes' if i1!=-1 and i1<i2 else 'No')