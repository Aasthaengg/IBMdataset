#

import sys
input=sys.stdin.readline

def main():
    S=input()
    mind=643
    for i in range(len(S)-2):
        mind=min(mind,abs(int(S[i:i+3])-753))
    print(mind)
    
    
    
if __name__=="__main__":
    main()
