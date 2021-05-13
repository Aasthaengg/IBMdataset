
import sys
input = sys.stdin.readline

def inp():
    return(int(input()))



n = inp()

print((n//1000+1)*1000-n) if n%1000 else print(0)