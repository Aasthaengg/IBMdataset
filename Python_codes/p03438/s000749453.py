import sys
input = sys.stdin.buffer.readline

def main():
    N = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    
    if sum(a) > sum(b):
        print("No")
    else:
        do = sum(b)-sum(a)
        ca,cb = 0,0
        for x,y in zip(a,b):
            if x > y:
                cb += x-y
            else:
                if (y-x)%2 == 0:
                    ca += (y-x)//2
                else:
                    ca += (y+1-x)//2
                    cb += 1
        if ca-cb >= 0:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()
