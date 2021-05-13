import math

#入力:N,M(int:整数)
def input2():
	return map(int,input().split())

def lcm(x, y):
	# 最小公倍数
    return (x * y) // math.gcd(x, y)


A,B,C,D=input2()
lenC=B//C
lenD=B//D
lenCD=B//lcm(C,D)

ans=0
ans=B-(lenC+lenD-lenCD)

A-=1
lenC=A//C
lenD=A//D
lenCD=A//lcm(C,D)

ans-=A-(lenC+lenD-lenCD)

print(ans)