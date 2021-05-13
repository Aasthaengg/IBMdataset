import sys
import random

def main():
    S = input()
    l = len(S)
    n = [0, 1, 2]
    out = S[n[0]] + S[n[1]] + S[n[2]]
    
    print(out)
main()