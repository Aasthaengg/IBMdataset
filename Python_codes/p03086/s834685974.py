a=[0]
for i in input():
 if i in "ACGT":a+=[a[-1]+1]
 else:a+=[0]
print(max(a))