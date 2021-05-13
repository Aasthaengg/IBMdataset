o,e=input(),input()
print(''.join(o[i//2]if i%2==0 else e[i//2]for i in range(len(o+e))))