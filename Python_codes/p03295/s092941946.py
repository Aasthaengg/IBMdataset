import sys
from operator import itemgetter
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
 
def main():
    N, M = map(int, readline().split())
    ab = map(int, read().split())
    ab = sorted(zip(ab, ab), key=itemgetter(1))
 
    east_island = ab[0][1]
    answer = 1
 
    for i, j in ab:
        if i >= east_island:
            answer += 1
            east_island = j
 
    print(answer)
 
 
if __name__ == '__main__':
    main()