import sys
input=sys.stdin.readline

def main():
    cnt = 0
    n = int(input())
    for i in range(1,n+1,2): # 奇数だけ繰り返す
        k = 0
        for m in range(1,i+1):
            if i % m == 0:
                k += 1
        if k == 8:
            cnt += 1
    print(cnt)

if __name__=="__main__":
    main()
