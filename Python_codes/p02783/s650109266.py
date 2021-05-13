import sys
import decimal # 10進法に変換，正確な計算

def input():
    return sys.stdin.readline().strip()

def main():
    h, a = map(int, input().split())
    count = 0
    while h > 0:
        h -= a
        count += 1
    print(count)
    

main()