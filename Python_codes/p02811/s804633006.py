import sys
import decimal # 10進法に変換，正確な計算

def input():
    return sys.stdin.readline().strip()

def main():
    k, x = map(int, input().split())
    if 500*k >= x:
        print("Yes")
        return
    print("No")

    
    
main()
