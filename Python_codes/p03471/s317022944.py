# N = int(input())

N,Y = map(int, input().split())   # 2つ整数の読み取り

# A = list(map(int, input().strip().split()))  # 横に何個か
 
# N=int(input())
# A=[int(input()) for _ in range(N)]  # 縦に一個ずつ

x,y,z = 0,0,0
total = 0
flg=0

for i in range(N+1):
    for j in range(0,N-i+1):
        if flg==0:
            x=i
            y=j
            z=N-x-y
            total = x*10000 + y*5000 + z*1000
            # print(total)
            # print(x,y,z)
    
            if total == Y:
                print(x,y,z)
                flg = 1

if flg == 0:
    print("-1 -1 -1")
