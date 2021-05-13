N, M = map(int, input().split())
Cset=M//2
num = min(N , Cset)
if Cset-N >= 2:
    num+=(Cset-N)//2
print(num)