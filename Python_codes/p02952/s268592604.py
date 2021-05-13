import sys

def main():
    N = int(input())
    
    cnt = 0
    for i in range(1, N+1):
        if 1 <= i < 10:
            cnt += 1
        elif 100 <= i < 1000:
            cnt += 1
        elif 10000 <= i < 100000:
            cnt += 1
                    
    print(cnt)
main()