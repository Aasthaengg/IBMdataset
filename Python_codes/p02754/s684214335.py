n,a,b = map(int,input().split())
'''
bbbbrrbbbbrr...
n // (a+b) : a+b個の塊がn個のなかにいくつ入っているか
n % (a+b)  : a+b個の列のうち、いくつまで入るか
'''

ans = n // (a+b) * a + min(n % (a+b), a)
print(ans)