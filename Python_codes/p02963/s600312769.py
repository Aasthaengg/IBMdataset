def main():
    S = int(input())
    v = 10**9
    ans = [0,0,10**9,1,(v-S%v)%v,(S+(v-S%v)%v)//v]
    print(*ans)

if __name__ == "__main__":
    main()