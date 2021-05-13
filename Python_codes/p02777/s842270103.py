import sys
import decimal # 10進法に変換，正確な計算

def input():
    return sys.stdin.readline().strip()

def main():
    s, t = input().split()
    a, b = map(int, input().split())
    u = input()
    if s == u:
        print(a-1,b)
        return
    print(a,b-1)

    
main()