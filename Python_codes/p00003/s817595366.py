import sys;
#from me.io import dup_file_stdin

#@dup_file_stdin
def solve():
    n=int(sys.stdin.readline())
    for i in range(n):
        x=[int(num) for num in sys.stdin.readline().split(' ')]
        x.sort();
        if(x[0]**2+x[1]**2==x[2]**2): print("YES")
        else :print("NO")
solve()