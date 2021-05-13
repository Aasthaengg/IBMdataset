"""
NTC here
"""
import sys
inp= sys.stdin.readline
input = lambda : inp().strip()
flush= sys.stdout.flush
# import threading
# setrecursionlimit(10**6)
# threading.stack_size(2**26)

def iin(): return int(input())
def lin(): return list(map(int, input().split()))

# range = xrange
# input = raw_input

def main():
    n, k = lin()
    print('YES' if k*2-1<=n else 'NO')





        
main()
#threading.Thread(target=main).start()