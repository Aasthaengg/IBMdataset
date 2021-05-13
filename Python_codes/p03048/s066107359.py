def main():
    R,G,B,N = map(int,input().split())
    cnt = 0

    for x in range(N//R+1):
        for y in range(N//G+1):
            z = N - R*x - G*y
            if z >= 0 and z % B == 0:
                cnt += 1
    print(cnt)

if __name__ == "__main__":
    main()