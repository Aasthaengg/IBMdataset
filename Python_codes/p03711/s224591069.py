A=[['1','3','5','7','8','10','12'],['4','6','9','11'],['2']]
x,y=input().split()
print(['No','Yes'][list(map(lambda z:x in z, A))==list(map(lambda z:y in z, A))])