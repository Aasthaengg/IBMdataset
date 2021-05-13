def main():
    N = int(input())
    ls = [[int(x) for x in input().split()] for _ in range(N)]
    ans = 0
    for i in range(N):
        ls[i].append(ls[i][0]+ls[i][1])
    ls = sorted(ls,key=lambda x:-x[2])
    if N==1:
        print(ls[0][1])
        exit()
    for i in range(N):
        ans -= ls[i][1]

    for i in range(N//2):
        ans += ls[2*i][2]

    if N%2==1:
        ans += ls[2*i+2][2]
    
    print(ans)
if __name__ == '__main__':
    main()