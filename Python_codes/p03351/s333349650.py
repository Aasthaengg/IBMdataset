import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

a,b,c,d = MI()
print('Yes' if (abs(a-b) <= d and abs(b-c) <= d) or abs(a-c) <= d else 'No')
