#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [input() for _ in range(n)]

a,b,c,d = map(int, input().split())

#b-a分を回してみるのは10**18なので間に合わない

#A以上B以下の整数でXで割り切れない個数を言い換えると
#Bが整数Xで割り切れない個数 - (A-1)が整数Xで割り切れない個数となる

#次にBが整数Xで割り切れない個数を考える。
#Bが整数Xで割り切れる個数は、B//Xなので、割り切れない個数は B-B//Xとなる

#次にBが整数XとYで割り切れない個数を考える
#B -B//X -B//Y + 2B//(X*Y)としたいところだが
#XとYでも割り切れるものは、B//(X*Y)ではなく、B//LCM(X,Y)となる
# X = 4, Y = 6だと 24で割り切れる個数となるが
# 12は、4と6でも割り切れるが24では割り切れない
#よってXとYの最小公倍数となる

import math

def lcm(x, y):
    return x // math.gcd(x, y) * y

def func(val, x, y):
    return val-val//x-val//y+val//lcm(x,y)

ans = (func(b,c,d)-func(a-1,c,d))
print(ans)

