import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
def main():
    n = int(readline())
    print(sum([int(i)-1 for i in readline().split()]))

if __name__ == '__main__':
    main()
