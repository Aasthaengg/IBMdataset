# B - A to Z String
def main():
    s = list(input())
    start = 0
    end = 0

    for i in range(len(s)):
        if s[i] == 'A':
            start = i
            break
    for j in range(len(s)-1, 0, -1):
        if s[j] == 'Z':
            end = j
            break
    
    print(end-start+1)


        
        
if __name__ == '__main__':
    main()