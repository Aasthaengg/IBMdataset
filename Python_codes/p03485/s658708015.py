
import math
def main():
    a, b = map(int, input().split())
    x = (a + b ) / 2
    x = math.ceil(x)
    print(x)
main()