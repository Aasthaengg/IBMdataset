def main():
    l,r,d = tuple([int(t)for t in input().split()])
    ans = 0
    for i in range(l,r+1):
        if i%d == 0:
            ans+=1
    print(ans)
    

if __name__ == "__main__":
    main()