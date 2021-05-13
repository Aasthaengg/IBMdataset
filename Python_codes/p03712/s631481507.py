import sys
def LI():
    return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def S(): 
    return sys.stdin.readline().rstrip()

H,W = LI()

print(''.join(['#']*(W+2)))

for i in range(H):
    print('#' + S() + '#')

print(''.join(['#']*(W+2)))