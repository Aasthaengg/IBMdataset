import sys
import decimal # 10進法に変換，正確な計算

def input():
    return sys.stdin.readline().strip()

def main():
    s = input()
    if s[0] == "S":
        print("Cloudy")
        return
    elif s[0] == "C":
        print("Rainy")
        return
    print("Sunny")
    

    
    
main()