import sys

def LS2(): 
    return list(sys.stdin.readline().rstrip())  #空白なし

n = LS2()

for i in range(3):
    if n[i] == '1':
        n[i] = '9'
    else:
        n[i] = '1'

print(''.join(n))