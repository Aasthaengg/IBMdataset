
from collections import deque
import sys

d=deque()

n=int(input())

for i in range(n):
    s=input()
    if s=='deleteFirst':
        d.popleft()
    elif s=='deleteLast':
        d.pop()
    else:
        ss,num=s.split()
        if ss == 'insert':
            d.appendleft(num)
        else:
            try:
                d.remove(num)
            except:
                pass

print(' '.join(d))

"""
def main():
    num2 = 5
    plus(num2)
    print(num2)

def plus(num2):
    num2 += 2
    return num2

if __name__=="__main__":
    main()
    """
