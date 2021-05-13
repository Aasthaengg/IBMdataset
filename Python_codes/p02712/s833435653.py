import math
def main():
    n = int(input())
    r = 0
    for x in range(1, n + 1):
        if x % 3 == 0 and x % 5 == 0:
            continue
        elif x % 3 == 0:
            continue
        elif x % 5 == 0:
            continue
        else:
            r += x
    
    print(r)

main()
