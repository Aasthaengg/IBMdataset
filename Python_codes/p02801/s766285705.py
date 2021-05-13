import sys
import decimal # 10進法に変換，正確な計算

def input():
    return sys.stdin.readline().strip()

def main():
    c =  input()
    a = "abcdefghijklmnopqrstuvwxyz"
    for i in range(25):
        if a[i] == c:
            print(a[i+1])
            return

main()

