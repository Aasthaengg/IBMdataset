import sys,math

def solve():
    while True:
        s = input()
        if "?" in s:
            break
        else:
            print(int(eval(s)//1))
    
solve()
