def main():
    N  = int(input())
    Ds = [list(map(int,input().split())) for _ in range(N)]
    count = 0
    for D in Ds:
        if D[0]==D[1]:
            count += 1
        else:
            count = 0
        if count == 3:
            print("Yes")
            return
    print("No")
    
main()