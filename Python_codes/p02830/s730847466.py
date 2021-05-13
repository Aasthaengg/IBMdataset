def main():
    n = int(input())
    s, t= map(str,input().split()) 
    a = ""
    for i in range(n):
        a += s[i]
        a += t[i]
    
    print(a)
    




    
if __name__ == "__main__":
    main()
