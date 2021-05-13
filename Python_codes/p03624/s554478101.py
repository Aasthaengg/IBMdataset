from collections import defaultdict,deque
import math
def main():
    alph = "abcdefghijklmnopqrstuvwxyz"
    s = input()

    for i in range(26):
        if(s.count(alph[i])==0):
            print(alph[i])
            exit()
    print("None")

if __name__ == '__main__':
    main()
