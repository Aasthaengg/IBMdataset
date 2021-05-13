import itertools

def main():
    n = int(input())
    d = map(int, input().split())
    
    h = 0
    for d1, d2 in itertools.combinations(d, 2):
        h += d1 * d2
    print(h)
    
if __name__ == '__main__':
    main()