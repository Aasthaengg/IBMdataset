import sys
import decimal # 10進法に変換，正確な計算

def input():
    return sys.stdin.readline().strip()

def main():
    s = input()
    if s[0] == "S":
        if s[1] == "U":
            print(7)
            return
        print(1)
        return
    elif s[0] == "F":
        print(2)
        return
    elif s[0] == "W":
        print(4)
        return
    elif s[0] == "M":
        print(6)
        return
    elif s[1] == "H":
        print(3)
        return
    print(5)
    
    
    
main()