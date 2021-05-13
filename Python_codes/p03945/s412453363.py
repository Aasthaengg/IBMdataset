def main():
    s = input()
    slen = len(s)
    cnt = 0
    last = 0
    if s[0] == "W":
        for i in range(slen-1):
            if s[i] == "W" and s[i+1] =="B":
                cnt += 1
        if s[-1] == "W":
            last = 1
    if s[0] == "B":
        for i in range(slen-1):
            if s[i] == "B" and s[i+1] =="W":
                cnt += 1
        if s[-1] == "B":
            last = 1        
    if cnt == 0:
        print(cnt)
    else:
        print(cnt*2 - 1 + last)
    

 
    
    
if __name__ == "__main__":
    main()