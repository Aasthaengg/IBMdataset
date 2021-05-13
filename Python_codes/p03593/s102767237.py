from collections import Counter

def main():
    H, W = map(int, input().split())
    all_c = Counter([])
    for _ in range(H):
        line = list(input())
        line_c = Counter(line)
        all_c += line_c
    
    if H % 2 == 0 and W % 2 == 0:
        if all(val%4 == 0 for val in all_c.values()):
            print("Yes")
        else:
            print("No")

    elif H % 2 ^ W % 2:
        flag = all(val%2 == 0 for val in all_c.values())
        two_count = sum(val%4 == 2 for val in all_c.values())

        if H % 2 == 0:
            threshould = H//2
        else:
            threshould = W//2

        if flag and two_count <= threshould:
            print("Yes")
        else:
            print("No")

    elif H % 2 == 1 and W % 2 == 1:
        one_count = sum(val%2 == 1 for val in all_c.values())
        
        three_count = sum(val%4 == 3 for val in all_c.values())
        two_count = sum(val%4 == 2 for val in all_c.values())

        threshould = H//2 + W//2
        if one_count == 1 and three_count + two_count <= threshould:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()