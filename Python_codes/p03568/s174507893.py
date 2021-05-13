N = int(input())
src = list(map(int,input().split()))
 
whole = 3**N
even = 0
for i in range(N):
    if src[i]%2 == 0: even += 1
 
print(whole - 2**even)