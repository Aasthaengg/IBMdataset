s=list(input())
w=int(input())
print(''.join([x for i,x in enumerate(s) if i%w==0]))