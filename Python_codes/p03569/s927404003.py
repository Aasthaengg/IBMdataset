import sys
#input = sys.stdin.buffer.readline

def main():
    s = input()
    l,r = 0,len(s)-1
    count = 0
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            if s[l] == "x":
                l += 1
            elif s[r] == "x":
                r -= 1
            else:
                print("-1")
                exit()
            count += 1
            
    print(count)
    
if __name__ == "__main__":
    main()