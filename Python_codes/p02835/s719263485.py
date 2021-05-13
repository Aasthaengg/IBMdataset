import sys
import decimal # 10進法に変換，正確な計算

def input():
    return sys.stdin.readline().strip()

def main():
    a = list(map(int, input().split())) 
    h = 0   
    for i in a:
        h += i
    if h >= 22:
        print("bust")
        return
    print("win")
    

main()
