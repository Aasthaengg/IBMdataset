import sys
input = sys.stdin.readline

N,A,B = map(int,input().split())
answer = 'Alice' if (B-A)%2==0 else 'Borys'
print(answer)