
def main():
    s = input()
    t = input()
    min = int(1e9)
    for i in range(len(s)-len(t)+1):
        cnt = 0
        for j in range(len(t)):
            if s[i+j] != t[j]:
                cnt += 1
        if min > cnt:
            min = cnt
    print(min)
            
if __name__ == "__main__":
    main()