import sys
import decimal # 10進法に変換，正確な計算

def input():
    return sys.stdin.readline().strip()

def main():
    n = int(input())
    d = list(map(int, input().split()))
    sum = 0
    for i in range(n-1):
        for k in range(i+1,n):
            sum += d[i]*d[k]
    print(sum)
    
    
main()
