import sys
import itertools
input = lambda: sys.stdin.readline().rstrip()

def main():
    dishes = [int(input()) for _ in range(5)]
    ans = float('inf')
    for dish in itertools.permutations(dishes, 5):
        time = 0
        for i in range(5):
            time += dish[i]
            if time%10 != 0 and i < 4:
                time += 10 - time%10
        ans = min(ans, time)
    print(ans)
            
if __name__ == '__main__':
    main()