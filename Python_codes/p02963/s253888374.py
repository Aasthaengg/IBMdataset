import math
def main():
    S = int(input())
    r = math.ceil(math.sqrt(S))
    print(0, 0, r, 1, r * r - S, r)

main()
