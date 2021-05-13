import sys
#import cython

def main():
    read = lambda: sys.stdin.readline().rstrip()
    
    #N: cython.longlong = 0
    N = read()
    print("ABC" if N[1]=="R" else "ARC")
 
if __name__ == "__main__":
    main()