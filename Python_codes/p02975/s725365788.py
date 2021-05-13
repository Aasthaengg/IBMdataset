from collections import Counter

def main():
    N = int(input())
    A = tuple(map(int, input().split()))
    
    c = Counter(A).most_common()
    
    if c[0][0] == 0 and c[0][1] == N:
        print("Yes")
    elif len(c) == 2 and c[0][1] == 2*N//3 and c[1][0] == 0 and c[1][1] == N//3:
        print("Yes")
    elif len(c) == 3 and int(c[0][0])^int(c[1][0]) == int(c[2][0]) and c[0][1] == c[1][1] and c[1][1] == c[2][1]:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()