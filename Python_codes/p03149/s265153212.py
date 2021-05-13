# coding: utf-8
# Your code here!

N = list(map(int, input().split()))

# print(N)

def hantei(N):
    if not 1 in N:
        return False
    if not 9 in N:
        return False
    if not 7 in N:
        return False
    if not 4 in N:
        return False
        
    return True
    
if hantei(N):
    print('YES')
else:
    print('NO')