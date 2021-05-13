import math
def main():
    S = int(input())
    t = int(math.sqrt(S))
    if t * t == S:
        print("0 0", t, "0 0", t)
        return
    x = (t+1) * (t+1) - S
    print("0 0 1", t+1, t+1, x)
    return
main()
    
