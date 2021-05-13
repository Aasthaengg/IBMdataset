o=input()
e=input()
mix=[o,e]
ans=[]
for i in range(len(o)+len(e)):
    ans.append(mix[i%2][i//2])
print(''.join(ans))