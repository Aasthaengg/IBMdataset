import itertools

def main():
    k,s=map(int,input().split())
    count = 0
    for x,y in itertools.product(range(k+1), repeat=2):
        if 0 <= s-(x+y) <= k:
            count += 1
    print(count)
        
if __name__ == "__main__":
    main()