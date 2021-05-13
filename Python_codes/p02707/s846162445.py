from collections import Counter

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a_c = Counter(a)
    for i in range(1, n+1):
        ans = a_c.get(i)
        if ans:
            print(ans)
        else:
            print(0)
        
if __name__ == '__main__':
    main()