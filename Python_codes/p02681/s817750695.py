import sys
input = sys.stdin.readline

def main():
    s = str( input() )
    t = str( input() )
    
    if s[:-1] == t[:-2]:
        print('Yes')
    else:
        print('No')



main()