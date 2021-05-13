import sys

def main():
    arr = sys.stdin.readline().rstrip("\n").split(" ")
    a = int(arr[0])
    b = int(arr[1])
    print a*b , a*2+b*2
    
main()