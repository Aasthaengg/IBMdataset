k = int(input())
a, b = list(map(int, input().split()))
s = [i for i in range(a, b+1) if i % k == 0]
if a == b and a % k == 0:
    print('OK')  
elif len(s)==0:
    print('NG')    
else:
    print('OK')

