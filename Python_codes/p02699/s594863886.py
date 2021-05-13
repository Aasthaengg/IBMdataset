import sys
S,W = map(int,input().split())

if not ( 1 <= S <= 100 and 1 <= W <= 100 ): sys.exit()

print('safe') if S > W else print('unsafe')