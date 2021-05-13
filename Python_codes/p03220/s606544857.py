def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))

    mindiff = pow(10, 6)
    for i in range(N):
        temprature = T - 0.006*H[i]
        diff = abs(temprature - A)
        if diff < mindiff:
            ans = i+1
            mindiff = diff
    
    print(ans)

if __name__ == "__main__":
    main()
