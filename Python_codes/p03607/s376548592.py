from collections import Counter

def main():
    a = Counter(int(input()) for _ in range(int(input())))
    ans=0
    for i,v in a.items():
        if v % 2 != 0:
            ans+=1
    print(ans)

if __name__ == "__main__":
    main()