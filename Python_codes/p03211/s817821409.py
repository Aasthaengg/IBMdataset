def main():
    s=input()
    d=[]
    for i in range(len(s)-2):
        d.append(abs(int(s[i:i+3])-753))
    print(min(d))
    
if __name__ == "__main__":
    main()