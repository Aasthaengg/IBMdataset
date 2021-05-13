#

import sys
from math import ceil
input=sys.stdin.readline

def main():
    t=[int(input()) for i in range(5)]
    tp10=[t[i]%10 for i in range(5) if t[i]%10!=0]
    ans=0
    for i in range(5):
        ans+=ceil(t[i]/10)*10
    if len(tp10)>0:
      	print(ans-10+min(tp10))
    else:
      	print(ans)
    
if __name__=="__main__":
    main()
