import sys
import decimal # 10進法に変換，正確な計算

def input():
    return sys.stdin.readline().strip()

def main():
    s = input()
    r = s[::-1]
    l = len(s)
    count = 0
    if l % 2 == 0:
        for i in range(l//2):
            if s[i] != r[i]:
                count += 1
        print(count)
        return
    for i in range(l//2 + 1):
        if s[i] != r[i]:
            count += 1
    print(count)
    

main()
