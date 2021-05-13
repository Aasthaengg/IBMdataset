import sys
def main():
    input = sys.stdin.readline
    N=int(input())
    *A,=map(int, input().split())
    *B,=map(int, input().split())

    opa=opb=0
    for a,b in zip(A,B):
        if a>=b:
            opb+=a-b
        else:
            if (b-a)&1==0:
                opa+=(b-a)//2
            else:
                opa+=(b-a)//2 + 1
                opb+=1

    print('Yes' if opa>=opb else 'No')

if __name__ == '__main__':
    main()