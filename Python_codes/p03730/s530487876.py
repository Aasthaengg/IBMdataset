def main():
    a,b,c=map(int,input().split())
    sumi = set()
    for i in range(10**9):
        x = a*i%b
        if x in sumi:
            break
        elif x == c:
            print("YES")
            return
        else:
            sumi.add(x)
    print("NO")
    
if __name__ == "__main__":
    main()