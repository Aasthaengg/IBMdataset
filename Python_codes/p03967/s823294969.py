import  sys
s=input()

a=s.count('g')
if len(s)/2==a:
    print('0')
    sys.exit()

if len(s)%2==0:
    p=a-len(s)/2
else:
    p=a-(len(s)+1)/2
print(int(p))