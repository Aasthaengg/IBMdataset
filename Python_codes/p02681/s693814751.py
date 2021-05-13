s=input()
t=input()

n=len(s)
if s==t[:len(s)]:
    print('Yes')
else:
    print('No')