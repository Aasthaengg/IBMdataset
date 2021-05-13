def main():
    n,m=map(int, input().split())
    k = [0]*n
    for i in range(m):
        a,b=map(int, input().split())
        k[a-1]+=1
        k[b-1]+=1
    for i in k:
        if i%2==1:
            print("NO")
            exit()
    print("YES")
if __name__ == '__main__':
    main()
