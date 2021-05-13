N = int(input())
mod = N % 1000
if mod == 0: print(0)
else: print(1000 - mod)
