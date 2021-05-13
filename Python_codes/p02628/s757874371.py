
import sys
input = sys.stdin.readline

    
def inlt():
    return(list(map(int,input().split())))


n, k = inlt()
p = inlt()
p = sorted(p)
print(sum(p[:k]))


