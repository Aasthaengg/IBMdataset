from collections import defaultdict

def main():
    dic = defaultdict(int)
    for _ in range(3):
        a,b = map(int,input().split())
        dic[a] += 1
        dic[b] += 1
    
    for i in range(1,5):
        if dic[i]==3:
            print("NO")
            exit()
    print("YES")
if __name__ == '__main__':
    main()