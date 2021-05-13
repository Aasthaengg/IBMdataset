import math

def main():
    A, B, H, M = map(int, input().split())
    rad = math.pi * 2 * (H / 12 + (M / 60)/ 12 - M / 60)
    rsq = (A * A + B * B) - (2 * A * B) * math.cos(rad)
    print(math.sqrt(rsq))
main()  