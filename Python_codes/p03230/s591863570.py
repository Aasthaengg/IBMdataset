import sys
input = sys.stdin.buffer.readline

def main():
    N = int(input())
    k = int((N*2)**(1/2))
    if N*2 != k*(k+1):
        print("No")
    else:
        print("Yes")
        l = [[0 for _ in range(k)] for _ in range(k+1)]
        for i in range(k):
            for j in range(k-i):
                if i == 0:
                    l[i][j] = j+1
                    l[j+1][i] = j+1
                else:
                    l[i][i+j] = 1+(k+1)*i-i*(i+1)//2+j
                    l[i+j+1][i] = 1+(k+1)*i-i*(i+1)//2+j
        print(k+1)
        for i in range(k+1):
            print(k,*l[i])

if __name__ == "__main__":
    main()