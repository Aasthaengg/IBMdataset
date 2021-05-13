def main():
    n=int(input())
    for i in range(26):
        if i*4 <= n and (n-i*4) % 7 == 0:
            print("Yes")
            return
    print("No")
    
if __name__ == "__main__":
    main()