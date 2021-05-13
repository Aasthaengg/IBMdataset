a,b = map(str, input().split())
one,two = map(int, input().split())
dis = input()

if dis == a: print(one-1, two)
else: print(one, two-1)