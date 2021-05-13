from itertools import combinations
MOD = 10**9+7

def main():
    N, k = map(int, input().split(' '))
    count = 0

    if k > N:
        print('1')
        exit(0)
    for i in range(k,N+2):
        maxsum = (N*(N+1) - (N-(i-1))*(N-i))//2
        minsum = (i-1)*i//2
        count += maxsum - minsum + 1

    print(count%MOD)



if __name__ == "__main__":
    main()
