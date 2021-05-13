n, y = list(map(int,input().split()))
def main():
    for i in range(n+1):
        for j in range(n+1-i):
            total = 10000*i+5000*j+1000*(n-i-j)
            if total == y:
                return print(i,j,n-i-j)
    return print('-1 -1 -1')

main()