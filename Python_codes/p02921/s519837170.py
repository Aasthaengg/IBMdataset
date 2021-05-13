import sys
import decimal # 10進法に変換，正確な計算

def input():
    return sys.stdin.readline().strip()

def main():
    s = input()
    t = input()
    count = 0
    for i in range(3):
        if s[i] == t[i]:
            count += 1
    print(count)    
    
main()
